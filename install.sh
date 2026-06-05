#!/usr/bin/env bash
set -euo pipefail

INSTALL_DIR="${AGINT_INSTALL_DIR:-$HOME/agint}"
WORK_DIR="${AGINT_WORK_DIR:-$INSTALL_DIR/work}"
REPO_URL="https://github.com/AgintAI/agint-cli.git"
MIN_PYTHON_VERSION="3.8"
PRESERVED_ENV_FILE=""
BACKUP_DIR=""

# Cleanup on failure: remove partially created install files
cleanup_on_failure() {
    if [ -d "$INSTALL_DIR/.venv" ] && [ "${INSTALL_COMPLETE:-0}" != "1" ]; then
        echo "" >&2
        echo "==> Installation failed. Cleaning up $INSTALL_DIR/.venv" >&2
        rm -rf "$INSTALL_DIR/.venv"
    fi
    if [ -n "$PRESERVED_ENV_FILE" ] && [ -f "$PRESERVED_ENV_FILE" ]; then
        rm -f "$PRESERVED_ENV_FILE"
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
    PRESERVED_ENV_FILE="$(mktemp)"
    cp "$INSTALL_DIR/.env" "$PRESERVED_ENV_FILE"
    chmod 600 "$PRESERVED_ENV_FILE" 2>/dev/null || true
fi

if [ -d "$INSTALL_DIR" ]; then
    timestamp="$(date +%Y%m%d%H%M%S)"
    BACKUP_DIR="${INSTALL_DIR}.backup.${timestamp}"
    echo "==> Existing installation found. Moving it to $BACKUP_DIR"
    mv "$INSTALL_DIR" "$BACKUP_DIR"
fi

# Create the install and work directories
mkdir -p "$INSTALL_DIR"
mkdir -p "$WORK_DIR"

if [ -n "$PRESERVED_ENV_FILE" ]; then
    cp "$PRESERVED_ENV_FILE" "$INSTALL_DIR/.env"
    chmod 600 "$INSTALL_DIR/.env" 2>/dev/null || true
fi

# Create and activate a virtual environment
python3 -m venv "$INSTALL_DIR/.venv"
source "$INSTALL_DIR/.venv/bin/activate"

# Install agint-cli from GitHub
pip install --upgrade pip
pip install "git+${REPO_URL}"

# Prompt for API configuration only when there was no preserved config
if [ ! -f "$INSTALL_DIR/.env" ]; then
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
else
    echo ""
    echo "==> Reusing existing API credentials from $INSTALL_DIR/.env"
fi

ln -sf "$INSTALL_DIR/.env" "$WORK_DIR/.env" 2>/dev/null || cp "$INSTALL_DIR/.env" "$WORK_DIR/.env"
chmod 600 "$WORK_DIR/.env" 2>/dev/null || true

if [ -n "$PRESERVED_ENV_FILE" ] && [ -f "$PRESERVED_ENV_FILE" ]; then
    rm -f "$PRESERVED_ENV_FILE"
fi

INSTALL_COMPLETE=1

echo ""
echo "==> Installation complete!"
echo ""
echo "Credentials saved to $INSTALL_DIR/.env"
if [ -n "$BACKUP_DIR" ]; then
    echo "Previous installation backed up to $BACKUP_DIR"
fi
echo "Default workspace created at $WORK_DIR"
echo ""
echo "To activate the environment and run commands from the workspace:"
echo ""
echo "  source $INSTALL_DIR/.venv/bin/activate"
echo "  cd $WORK_DIR"
echo ""
echo "Available commands: dagify, dagent, schemagin, datagin, agicat, agiwrite"

echo ""
read -rp "Open an activated shell in $WORK_DIR now? [y/N]: " enter_shell </dev/tty
if [[ "$enter_shell" =~ ^[Yy]$ ]]; then
    echo ""
    echo "==> Opening an activated shell in $WORK_DIR"
    echo "    Run 'exit' when you want to return to your previous shell."
    cd "$WORK_DIR"
    # shellcheck disable=SC1091
    source "$INSTALL_DIR/.venv/bin/activate"
    exec "${SHELL:-/bin/bash}" -i
fi
