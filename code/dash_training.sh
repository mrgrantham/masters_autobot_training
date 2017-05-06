#!/bin/bash

SESSION_NAME="dash_training"

tmux new-session -s ${SESSION_NAME} -n 'cd ~/autobot/code' 

tmux split-window -v 'watch -n 1 nvidia-smi' -t ${SESSION_NAME}
tmux split-window -h htop  -t ${SESSION_NAME}

tmux attach -t ${SESSION_NAME}