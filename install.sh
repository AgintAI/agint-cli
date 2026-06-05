#!/usr/bin/env bash
set -euo pipefail

INSTALL_DIR="${AGINT_INSTALL_DIR:-$HOME/agint}"
REPO_URL="https://github.com/AgintAI/agint-cli.git"
MIN_PYTHON_VERSION="3.8"

# Cleanup on failure: remove partially created install directory
cleanup_on_failure() {
    if [ -d "$INSTALL_DIR/.venv" ] && [ "${INSTALL_COMPLETE:-0}" != "1" ]; then
        echo "" >&2
        echo "==> Installation failed. Cleaning up $INSTALL_DIR/.venv" >&2
        rm -rf "$INSTALL_DIR/.venv"
    fi
}
trap cleanup_on_failure EXIT

# --- Prerequisite checks ---

# Check for python3
if ! command -v python3 &>/dev/null; then
    echo "Error: python3 is not installed. Please install Python ${MIN_PYTHON_VERSION}+ first." >&2
    exit 1
fi

# Check minimum Python version
python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" 2>/dev/null; then
    : # version OK
else
    echo "Error: Python ${MIN_PYTHON_VERSION}+ is required, but found ${python_version}." >&2
    exit 1
fi

# Check for git
if ! command -v git &>/dev/null; then
    echo "Error: git is not installed. It is required to install agint-cli." >&2
    exit 1
fi

# Check for pip/venv module availability
if ! python3 -c "import venv" 2>/dev/null; then
    echo "Error: Python venv module is not available. On Debian/Ubuntu, install it with:" >&2
    echo "  sudo apt install python3-venv" >&2
    exit 1
fi

echo "==> Installing agint-cli into $INSTALL_DIR (Python ${python_version})"

# --- Handle existing installation ---

if [ -f "$INSTALL_DIR/.env" ]; then
    echo ""
    echo "Warning: An existing configuration was found at $INSTALL_DIR/.env"
    read -rp "Overwrite existing config? [y/N]: " overwrite </dev/tty
    if [[ ! "$overwrite" =~ ^[Yy]$ ]]; then
        KEEP_ENV=1
    fi
fi

# Create the install directory
mkdir -p "$INSTALL_DIR"

# Create and activate a virtual environment
python3 -m venv "$INSTALL_DIR/.venv"
source "$INSTALL_DIR/.venv/bin/activate"

# Install agint-cli from GitHub
pip install --upgrade pip
pip install "git+${REPO_URL}"

# Prompt for API configuration (skip if keeping existing config)
if [ "${KEEP_ENV:-0}" != "1" ]; then
    echo ""
    echo "==> Configure your API credentials"
    echo ""

    read -rp "API URL [https://api.agintai.com]: " api_url </dev/tty
    api_url="${api_url:-https://api.agintai.com}"

    read -rp "API Key: " api_key </dev/tty
    if [ -z "$api_key" ]; then
        echo "Warning: No API key provided. You can set AGINT_APIKEY later."
    fi

    # Write .env file with restricted permissions
    (
        umask 077
        cat > "$INSTALL_DIR/.env" <<EOF
DOCKER_BUILDER_API_URL=${api_url}
AGINT_APIKEY=${api_key}
EOF
    )
fi

INSTALL_COMPLETE=1

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
