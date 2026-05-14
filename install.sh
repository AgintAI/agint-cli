#!/usr/bin/env bash
set -euo pipefail

INSTALL_DIR="${AGINT_INSTALL_DIR:-$HOME/agint}"
REPO_URL="https://github.com/AgintAI/agint-cli.git"

echo "==> Installing agint-cli into $INSTALL_DIR"

# Create the install directory
mkdir -p "$INSTALL_DIR"

# Create and activate a virtual environment
python3 -m venv "$INSTALL_DIR/.venv"
source "$INSTALL_DIR/.venv/bin/activate"

# Install agint-cli from GitHub
pip install --upgrade pip
pip install "git+${REPO_URL}"

# Prompt for API configuration
echo ""
echo "==> Configure your API credentials"
echo ""

read -rp "API URL [https://api.agintai.com]: " api_url </dev/tty
api_url="${api_url:-https://api.agintai.com}"

read -rp "API Key: " api_key </dev/tty
if [ -z "$api_key" ]; then
    echo "Warning: No API key provided. You can set AGINT_APIKEY later."
fi

# Write .env file
cat > "$INSTALL_DIR/.env" <<EOF
DOCKER_BUILDER_API_URL=${api_url}
AGINT_APIKEY=${api_key}
EOF

echo ""
echo "==> Installation complete!"
echo ""
echo "Credentials saved to $INSTALL_DIR/.env"
echo ""
echo "To activate the environment, run:"
echo ""
echo "  source $INSTALL_DIR/.venv/bin/activate"
echo ""
echo "Available commands: dagify, dagent, schemagin, datagin"
