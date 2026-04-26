#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${PROJECT_ROOT}/.venv"
TOOLS_DIR="${PROJECT_ROOT}/tools"

ask_yes_no() {
  local prompt="$1"
  local default="${2:-n}"
  local answer

  if [[ "${default}" == "y" ]]; then
    read -r -p "${prompt} [Y/n] " answer || true
    answer="${answer:-y}"
  else
    read -r -p "${prompt} [y/N] " answer || true
    answer="${answer:-n}"
  fi

  [[ "${answer}" =~ ^[Yy]$ ]]
}

echo "Project VIC Agentic AI Development Template setup for macOS"
echo "Project root: ${PROJECT_ROOT}"
echo
echo "Default behavior: install Python tools into a local virtual environment at ${VENV_DIR}."
echo

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 was not found. Install Python 3.11+ before continuing."
  echo "Homebrew users can run: brew install python"
  exit 1
fi

if ask_yes_no "Install recommended tools with Homebrew if brew is available?" "n"; then
  if command -v brew >/dev/null 2>&1; then
    brew install git gh python pipx
  else
    echo "Homebrew was not found. See https://brew.sh/ or install tools manually."
  fi
fi

if [[ ! -d "${VENV_DIR}" ]]; then
  python3 -m venv "${VENV_DIR}"
fi

# shellcheck source=/dev/null
source "${VENV_DIR}/bin/activate"
python -m pip install --upgrade pip

if ask_yes_no "Install uv into the local virtual environment?" "y"; then
  python -m pip install --upgrade uv
fi

mkdir -p "${TOOLS_DIR}"

if ask_yes_no "Install GitHub spec-kit into the local virtual environment?" "y"; then
  python -m pip install "git+https://github.com/github/spec-kit.git"
  echo "Verify with: ${VENV_DIR}/bin/specify version"
fi

if ask_yes_no "Clone Karpathy AutoResearch into tools/autoresearch? This is optional and GPU-oriented." "n"; then
  if [[ ! -d "${TOOLS_DIR}/autoresearch" ]]; then
    git clone https://github.com/karpathy/autoresearch.git "${TOOLS_DIR}/autoresearch"
  else
    echo "tools/autoresearch already exists; skipping clone."
  fi
fi

if ask_yes_no "Install CASE/UCO SDK Python package into the local virtual environment?" "y"; then
  python -m pip install --upgrade case-uco || {
    echo "case-uco package install failed. You can still clone the SDK repository in the next step."
  }
fi

if ask_yes_no "Clone CASE-UCO-SDK into tools/CASE-UCO-SDK for SDK and MCP server files?" "y"; then
  if [[ ! -d "${TOOLS_DIR}/CASE-UCO-SDK" ]]; then
    git clone https://github.com/vulnmaster/CASE-UCO-SDK.git "${TOOLS_DIR}/CASE-UCO-SDK"
  else
    echo "tools/CASE-UCO-SDK already exists; skipping clone."
  fi
fi

if command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is installed: $(gh --version | head -n 1)"
else
  echo "GitHub CLI was not found. See docs/github-setup.md or https://cli.github.com/."
fi

echo
echo "Setup complete."
echo "Activate the local Python environment with:"
echo "source .venv/bin/activate"

