#!/usr/bin/env bash
# Gracefully stops a run started by run_experiments.sh. It interrupts the notebook kernel (like Jupyter's
# stop button): the run in progress saves a checkpoint, then papermill exits. Re-run ./run_experiments.sh to resume.
set -uo pipefail
cd "$(dirname "$0")"
root=$(cat runs/latest.pid 2>/dev/null) || { echo "no runs/latest.pid"; exit 1; }
kill -0 "$root" 2>/dev/null || { echo "run $root is not running"; exit 0; }

descendants() { for c in $(pgrep -P "$1"); do echo "$c"; descendants "$c"; done; }
tree=$(descendants "$root")

# the kernel is the ipykernel process whose parent is not itself a kernel (env workers are forks of it)
kernel=""
for p in $tree; do
    parent=$(ps -o ppid= -p "$p" | tr -d ' ')
    if grep -q ipykernel_launcher "/proc/$p/cmdline" 2>/dev/null && \
       ! grep -q ipykernel_launcher "/proc/$parent/cmdline" 2>/dev/null; then
        kernel=$p
    fi
done

if [ -n "$kernel" ]; then
    echo "interrupting kernel $kernel (saving checkpoint)..."
    kill -INT "$kernel"
    for _ in $(seq 1 120); do
        kill -0 "$root" 2>/dev/null || { echo "stopped cleanly; re-run ./run_experiments.sh to resume"; exit 0; }
        sleep 1
    done
    echo "still running after 2 min, terminating"
fi
kill $tree "$root" 2>/dev/null
sleep 2
kill -9 $tree "$root" 2>/dev/null
echo "stopped"
