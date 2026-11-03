#!/usr/bin/env python
"""Watch a trained agent play, live in a game window and/or saved as a GIF.

Uses the same preprocessing as the notebook (frame skip 4, 2x downsample, grayscale, 4-frame stack), so the agent
sees exactly what it saw during training and testing. Works while training or testing runs in another terminal.

Examples
  python watch_agent.py --level 1-2 --model spatial --seed 42                  # on its own level
  python watch_agent.py --level 1-2 --model spatial --seed 42 --test-level 1-3 # on a level it never saw
  python watch_agent.py --level 1-3 --model baseline --seed 123 --record       # also save results/videos/*.gif
  python watch_agent.py --level 1-1 --model spatial --seed 42 --speed 2        # 2x speed
  python watch_agent.py --random --test-level 1-1                              # random policy, for comparison
Close the window or press Ctrl-C to stop.
"""
import argparse, re, sys, time
from collections import deque
from importlib.metadata import version
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
NES_FPS = 60.0988
SKIP, STACK = 4, 4


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--level", default="1-1", help="level the model was TRAINED on (picks the checkpoint)")
    p.add_argument("--model", default="spatial", choices=["baseline", "channel", "spatial", "pointwise"])
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--test-level", default=None, help="level to PLAY (default: the training level)")
    p.add_argument("--random", action="store_true", help="play a uniform random policy instead of a model")
    p.add_argument("--episodes", type=int, default=3)
    p.add_argument("--speed", type=float, default=1.0, help="1 = real game speed, 0 = as fast as possible")
    p.add_argument("--deterministic", action="store_true", help="always take the most likely action")
    p.add_argument("--record", action="store_true", help="save the episodes as results/videos/*.gif")
    p.add_argument("--no-window", action="store_true", help="do not open a window (e.g. on a server); use with --record")
    p.add_argument("--max-steps", type=int, default=3000, help="decisions per episode before giving up")
    p.add_argument("--checkpoint", default=None, help="explicit .zip path (overrides --level/--model/--seed)")
    return p.parse_args()


def find_checkpoint(level, model, seed):
    d = ROOT / "checkpoints" / level / f"{model}_s{seed}"
    final = d / f"{level}_{model}_s{seed}_final.zip"
    if final.exists():
        return final
    steps = [(int(m.group(1)), f) for f in d.glob("*.zip") if (m := re.search(r"_(\d+)_steps\.zip$", f.name))]
    if not steps:
        sys.exit(f"no checkpoint found in {d}")
    return max(steps)[1]


class Game:
    """One Mario level; steps with frame skip, renders every frame, keeps the agent's 4-frame stack."""

    def __init__(self, level, window, speed):
        import gym_super_mario_bros
        from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
        from nes_py.wrappers import JoypadSpace
        self.legacy = int(version("nes-py").split(".")[0]) < 9
        kwargs = {} if self.legacy or not window else {"render_mode": "human"}
        self.env = JoypadSpace(gym_super_mario_bros.make(f"SuperMarioBros-{level}-v0", **kwargs), SIMPLE_MOVEMENT)
        self.actions = ["+".join(a) for a in SIMPLE_MOVEMENT]
        self.window, self.frame_time = window, (1.0 / (NES_FPS * speed) if speed > 0 else 0.0)
        self.stack = deque(maxlen=STACK)

    @staticmethod
    def prep(frame):                                   # identical to MarioEnv._prep in the notebook
        small = frame[::2, ::2].astype(np.float32)
        return (small[..., 0] * 0.299 + small[..., 1] * 0.587 + small[..., 2] * 0.114).astype(np.uint8)

    def obs(self):                                     # (1, 120, 128, 4), like VecFrameStack
        return np.stack(self.stack, axis=-1)[None]

    def show(self):
        if self.window:
            self.env.render()

    def reset(self):
        out = self.env.reset()
        frame = out[0] if isinstance(out, tuple) else out
        self.stack.extend([np.zeros((120, 128), np.uint8)] * (STACK - 1) + [self.prep(frame)])
        self.show()
        return frame

    def step(self, action):
        done, info = False, {}
        for _ in range(SKIP):
            t0 = time.perf_counter()
            out = self.env.step(int(action))
            frame, info = out[0], out[-1]
            done = bool(out[2]) if len(out) == 4 else bool(out[2] or out[3])
            self.show()
            if self.frame_time:
                time.sleep(max(0.0, self.frame_time - (time.perf_counter() - t0)))
            if done:
                break
        self.stack.append(self.prep(frame))
        return frame, done, info

    def close(self):
        self.env.close()


def annotate(frame, text):
    from PIL import Image, ImageDraw
    img = Image.fromarray(frame).resize((frame.shape[1] * 2, frame.shape[0] * 2), Image.NEAREST)
    d = ImageDraw.Draw(img)
    d.rectangle([0, img.height - 22, img.width, img.height], fill=(0, 0, 0))
    d.text((6, img.height - 18), text, fill=(255, 255, 255))
    return img.convert("P", palette=Image.Palette.ADAPTIVE)


def main():
    a = parse_args()
    test_level = a.test_level or a.level
    if a.no_window and not a.record:
        sys.exit("--no-window without --record would show nothing; add --record")

    if a.random:
        model, name = None, "random policy"
    else:
        from stable_baselines3 import PPO
        ckpt = Path(a.checkpoint) if a.checkpoint else find_checkpoint(a.level, a.model, a.seed)
        model = PPO.load(ckpt, device="cpu")
        name = f"{a.model} s{a.seed} (trained on {a.level})"
        print(f"loaded {ckpt.relative_to(ROOT) if ckpt.is_relative_to(ROOT) else ckpt}")
    print(f"playing {test_level}: {name}" + ("  [UNSEEN LEVEL]" if not a.random and test_level != a.level else ""))

    rng = np.random.default_rng(a.seed)
    game = Game(test_level, window=not a.no_window, speed=a.speed)
    frames, results = [], []
    try:
        for ep in range(1, a.episodes + 1):
            frame, done, info, max_x, t = game.reset(), False, {}, 0, 0
            while not done and t < a.max_steps:
                if model is None:
                    action = int(rng.integers(len(game.actions)))
                else:
                    action = int(model.predict(game.obs(), deterministic=a.deterministic)[0][0])
                frame, done, info = game.step(action)
                t += 1
                max_x = max(max_x, info.get("x_pos", 0))
                if a.record:
                    frames.append(annotate(frame, f"{name} | level {test_level} | ep {ep} | x {info.get('x_pos', 0)}"
                                                  f" | {game.actions[action]}"))
            flag = bool(info.get("flag_get", False))
            results.append((ep, t, max_x, flag))
            print(f"episode {ep}: {t} decisions, max x {max_x}" + ("  FLAG!" if flag else ""))
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        game.close()

    if results:
        print(f"mean max x over {len(results)} episodes: {np.mean([r[2] for r in results]):.0f}")
    if a.record and frames:
        out = ROOT / "results" / "videos"
        out.mkdir(parents=True, exist_ok=True)
        who = "random" if a.random else f"{a.model}_s{a.seed}_trained{a.level}"
        path = out / f"{who}_on{test_level}.gif"
        frames[0].save(path, save_all=True, append_images=frames[1:], duration=int(1000 * SKIP / NES_FPS), loop=0,
                       optimize=True)
        print(f"saved {path.relative_to(ROOT)} ({len(frames)} frames, {path.stat().st_size / 2**20:.1f} MB)")


if __name__ == "__main__":
    main()
