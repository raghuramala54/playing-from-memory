#!/usr/bin/env bash
# Runs the whole notebook headless in the background: trains the experiment matrix, then writes every
# figure/table to results/. Resumable: re-running skips finished runs and continues unfinished ones.
#
#   ./run_experiments.sh                                # full matrix (3 levels × 3 variants × 3 seeds)
#   ./run_experiments.sh -p N_ENVS 12                   # any notebook parameter can be overridden
#   ./run_experiments.sh -y 'VARIANTS: [baseline, channel, spatial, pointwise]'
#   ./run_experiments.sh -p TRAIN False                 # regenerate results only, no training
#   NOTEBOOK=Mario_RL_Generalization.ipynb ./run_experiments.sh   # v2 generalisation study
#   NOTEBOOK=Mario_RL_Audit.ipynb ./run_experiments.sh            # diagnostic audit of saved models (no training)
#   NOTEBOOK=Atari_CLI_Audit.ipynb ./run_experiments.sh           # closed-loop index on published Atari agents
#
# Follow progress:  tail -f runs/latest.log        Stop (saves a checkpoint):  ./stop_experiments.sh
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p runs

NOTEBOOK="${NOTEBOOK:-Mario_RL_Attention_Research.ipynb}"   # NOTEBOOK=Mario_RL_Generalization.ipynb ./run_experiments.sh
stamp=$(date +%Y%m%d_%H%M%S)
log="runs/run_${stamp}.log"
out="runs/executed_${stamp}.ipynb"

# keep the machine awake while training (an earlier run lost ~5.5 h to a suspended laptop)
inhibit=()
if command -v systemd-inhibit >/dev/null 2>&1 && systemd-inhibit --what=idle true >/dev/null 2>&1; then
    inhibit=(systemd-inhibit --what=sleep:idle --who=mario-rl --why="RL training")
fi

nohup "${inhibit[@]}" papermill "$NOTEBOOK" "$out" \
    --log-output --no-progress-bar --request-save-on-cell-execute "$@" > "$log" 2>&1 &

echo $! > runs/latest.pid
ln -sf "$(basename "$log")" runs/latest.log
echo "started (pid $(cat runs/latest.pid))"
echo "  log:      $log   (tail -f runs/latest.log)"
echo "  notebook: $out"
