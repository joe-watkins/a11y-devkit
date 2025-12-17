#!/bin/bash
# Setup script for MagentaA11y skill submodule

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔧 Setting up MagentaA11y submodule..."

# Check if repo directory already exists
if [ -d "repo" ]; then
    echo "📦 Submodule already exists, updating..."
    git submodule update --remote repo
else
    echo "📥 Adding MagentaA11y submodule..."
    git submodule add https://github.com/tmobile/magentaA11y.git repo
fi

echo "✅ MagentaA11y skill setup complete!"
echo "📂 Documentation available at: repo/public/content/documentation/"
