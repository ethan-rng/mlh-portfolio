#!/bin/bash

# ARCHIVED
# Ending All Exisiting Tmux sessions
# tmux kill-server && echo "1. Killed All Running Servers Successfully"

cd ~/mlh-portfolio

# Fetching From Github
git fetch && git reset origin/main --hard && echo "2. Grabbed Remote Branch Successfully"

# Spin containers down then back up
docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build


# ARCHIVED CODE
# Starting Up Virtual Env and Installing Dependecies
# source python3-virtualenv/bin/activate && pip install -r "requirements.txt" && echo "3. Activated Virtual Env and Updated Dependencies"

# Creating New Tmux Session and Starting Flask Server
# tmux new-session -d -s my_flask_session 'flask run --host=0.0.0.0 --port=80'

# Starting Up myportfolio Service
# systemctl daemon-reload && systemctl restart myportfolio && echo "3. Restarted the myportfolio Service"
