#!/usr/bin/env bash
# Creates the Python environments for this repository.
#
#   ./setup.sh mario          # .venv        : Mario training + audit (GPU PyTorch if available)
#   ./setup.sh atari          # .venv-atari  : Atari closed-loop audit (CPU-only PyTorch, small download)
#   ./setup.sh all            # both
#   ./setup.sh mario --cpu    # CPU-only PyTorch for the Mario environment too
#
# Then: source .venv/bin/activate   (or .venv-atari/bin/activate)
set -euo pipefail
cd "$(dirname "$0")"

target="${1:-all}"; cpu="${2:-}"
PY="${PYTHON:-python3}"

if ! "$PY" -m venv --help >/dev/null 2>&1 || ! "$PY" -c "import ensurepip" >/dev/null 2>&1; then
    echo "Python venv support is missing. On Ubuntu/Debian run:  sudo apt install python3-venv python3-full"; exit 1
fi

make_env() {   # make_env <dir> <requirements file> <torch: gpu|cpu>
    local dir="$1" req="$2" torch="$3"
    [ -d "$dir" ] || "$PY" -m venv "$dir"
    "$dir/bin/python" -m pip install -q --upgrade pip
    if [ "$torch" = "cpu" ]; then
        "$dir/bin/pip" install -q torch --index-url https://download.pytorch.org/whl/cpu
    else
        "$dir/bin/pip" install -q torch
    fi
    "$dir/bin/pip" install -q -r "$req"
    "$dir/bin/python" -c "import torch; print('$dir: torch', torch.__version__, '| CUDA available:', torch.cuda.is_available())"
}

case "$target" in
    mario) make_env .venv requirements.txt "$([ "$cpu" = "--cpu" ] && echo cpu || echo gpu)" ;;
    atari) make_env .venv-atari requirements-atari.txt cpu ;;
    all)   make_env .venv requirements.txt "$([ "$cpu" = "--cpu" ] && echo cpu || echo gpu)"
           make_env .venv-atari requirements-atari.txt cpu ;;
    *)     echo "usage: ./setup.sh [mario|atari|all] [--cpu]"; exit 1 ;;
esac
echo "done. Activate with: source .venv/bin/activate  (Mario)  or  source .venv-atari/bin/activate  (Atari)"
