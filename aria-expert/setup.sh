#!/bin/bash
# Setup script for ARIA Expert skill

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

ARIA_SPEC_URL="https://github.com/w3c/aria.git"
APG_URL="https://github.com/w3c/aria-practices.git"

ARIA_DIR="repo/aria"
APG_DIR="repo/apg"

echo "🔧 Setting up W3C ARIA repositories..."

# Create repo directory if it doesn't exist
mkdir -p repo

# Clone/update main ARIA spec
if [ -d "$ARIA_DIR" ]; then
    echo "📦 ARIA spec exists, pulling latest..."
    cd "$ARIA_DIR"
    git pull origin main || git pull origin master
    cd ../..
else
    echo "📥 Cloning W3C ARIA specification..."
    git clone --depth 1 "$ARIA_SPEC_URL" "$ARIA_DIR"
fi

# Clone/update APG
if [ -d "$APG_DIR" ]; then
    echo "📦 APG exists, pulling latest..."
    cd "$APG_DIR"
    git pull origin main || git pull origin master
    cd ../..
else
    echo "📥 Cloning ARIA Authoring Practices Guide..."
    git clone --depth 1 "$APG_URL" "$APG_DIR"
fi

echo "✅ ARIA Expert skill setup complete!"
echo "📂 Content available at:"
echo "   - Main ARIA spec: repo/aria/index.html"
echo "   - Accessible Name spec: repo/aria/accname/index.html"
echo "   - Core AAM: repo/aria/core-aam/index.html"
echo "   - HTML AAM: repo/aria/html-aam/index.html"
echo "   - APG Patterns: repo/apg/content/patterns/"
echo "   - 5 Rules of ARIA: See SKILL.md"
