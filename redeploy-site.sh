#!/bin/bash

# Kill all existing tmux sessions
echo "Killing all existing tmux sessions..."
tmux kill-server

# Navigate to the project directory
echo "Navigating to the project directory..."
cd /root/mlh-portfolio || { echo "Failed to navigate to project directory"; exit 1; }

# Fetch the latest changes from the main branch on GitHub
echo "Fetching the latest changes from the main branch..."
git fetch && git reset origin/main --hard || { echo "Failed to fetch and reset git repository"; exit 1; }

# Activate the Python virtual environment and install dependencies
echo "Activating the Python virtual environment..."
source /root/mlh-portfolio/python3-virtualenv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }

echo "Installing Python dependencies..."
pip install -r requirements.txt || { echo "Failed to install Python dependencies"; exit 1; }

# Set Flask environment variables
echo "Setting Flask environment variables..."
export FLASK_ENV=development
export FLASK_APP=app/__init__.py

# Start a new detached tmux session that runs the Flask server
echo "Starting a new detached tmux session for the Flask server..."
tmux new-session -d -s my_flask_session 'cd /root/mlh-portfolio && source /root/mlh-portfolio/python3-virtualenv/bin/activate && flask run --host=0.0.0.0'

# Verify if the tmux session is running
tmux ls | grep my_flask_session > /dev/null
if [ $? -eq 0 ]; then
  echo "Deployment completed successfully. Flask server is running in tmux session 'my_flask_session'."
else
  echo "Failed to start the Flask server in tmux session 'my_flask_session'."
  exit 1
fi
