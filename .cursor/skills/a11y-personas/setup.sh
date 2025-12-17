#!/bin/bash
# Setup script for A11y Personas skill submodule

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔧 Setting up A11y Personas submodule..."

# Check if repo directory already exists
if [ -d "repo" ]; then
    echo "📦 Submodule already exists, updating..."
    git submodule update --remote repo
else
    echo "📥 Adding A11y Personas submodule..."
    git submodule add https://github.com/joe-watkins/a11y-personas.git repo
fi

echo "✅ A11y Personas skill setup complete!"
echo "📂 Personas available at: repo/data/personas/"

