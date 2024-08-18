

#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Echo each command being executed (optional, useful for debugging)
set -x

# Update and install system dependencies (if any)
apt-get update && apt-get install -y libffi-dev libssl-dev

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install --force-reinstall -U setuptools

# Additional steps (optional)
# If you need to set up something like database migrations, collect static files, etc., you can add that here.

# Example: Running a script to check if all dependencies are installed correctly
python -c "import flask, numpy, pickle; print('Dependencies are installed correctly.')"

echo "Build script executed successfully."
