#!/bin/bash
# Setup script for WCAG Expert skill submodule

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔧 Setting up W3C WCAG submodule..."

# Check if repo directory already exists
if [ -d "repo" ]; then
    echo "📦 Submodule already exists, updating..."
    git submodule update --remote repo
else
    echo "📥 Adding W3C WCAG submodule..."
    git submodule add https://github.com/w3c/wcag.git repo
fi

echo "✅ WCAG Expert skill setup complete!"
echo "📂 Content available at:"
echo "   - Understanding docs: repo/understanding/"
echo "   - Techniques: repo/techniques/"
echo "   - Guidelines: repo/guidelines/"

