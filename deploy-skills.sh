#!/bin/bash

# Deploy A11y Skills to IDE-specific locations
# This script symlinks skills to .claude/skills/, .cursor/skills/, and .github/skills/
# allowing you to test different IDE integrations without duplicating skill files.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGES_DIR="$SCRIPT_DIR/packages"
cd "$SCRIPT_DIR"

# IDE target directories
CLAUDE_DIR=".claude/skills"
CURSOR_DIR=".cursor/skills"
GITHUB_DIR=".github/skills"

# Deployment mode: copy (default) or symlink
DEPLOY_MODE="copy"

# IDEs to deploy to (default: all)
DEPLOY_CLAUDE=false
DEPLOY_CURSOR=false
DEPLOY_GITHUB=false
DEPLOY_ALL=false

# Setup external resources
RUN_SETUP=false

# Show help
show_help() {
    cat << EOF
Usage: ./deploy-skills.sh [OPTIONS]

Deploy A11y Skills to IDE-specific directories.

OPTIONS:
    --all               Deploy to all IDEs (default if no IDE specified)
    --claude            Deploy to Claude Code (.claude/skills/)
    --cursor            Deploy to Cursor (.cursor/skills/)
    --github            Deploy to GitHub Copilot (.github/skills/)

    --symlink           Use symlinks instead of copying files (default: copy)
    --setup             Run setup.sh scripts for skills that have them

    --clean             Remove all IDE deployment directories
    --list              List all available skills

    -h, --help          Show this help message

EXAMPLES:
    ./deploy-skills.sh --all                    # Deploy to all IDEs (copy files)
    ./deploy-skills.sh --claude --setup         # Deploy to Claude with setup
    ./deploy-skills.sh --cursor --symlink       # Deploy to Cursor (use symlinks)
    ./deploy-skills.sh --clean                  # Remove all IDE directories
    ./deploy-skills.sh --list                   # List all skills

EOF
}

# Parse command line arguments
parse_args() {
    if [ $# -eq 0 ]; then
        DEPLOY_ALL=true
    fi

    while [ $# -gt 0 ]; do
        case "$1" in
            --all)
                DEPLOY_ALL=true
                shift
                ;;
            --claude)
                DEPLOY_CLAUDE=true
                shift
                ;;
            --cursor)
                DEPLOY_CURSOR=true
                shift
                ;;
            --github)
                DEPLOY_GITHUB=true
                shift
                ;;
            --symlink)
                DEPLOY_MODE="symlink"
                shift
                ;;
            --setup)
                RUN_SETUP=true
                shift
                ;;
            --clean)
                clean_deployments
                exit 0
                ;;
            --list)
                list_skills
                exit 0
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                echo -e "${RED}Error: Unknown option '$1'${NC}"
                show_help
                exit 1
                ;;
        esac
    done

    # If --all or no specific IDE selected, deploy to all
    if [ "$DEPLOY_ALL" = true ]; then
        DEPLOY_CLAUDE=true
        DEPLOY_CURSOR=true
        DEPLOY_GITHUB=true
    fi
}

# Find all skills (directories with SKILL.md in packages/)
find_skills() {
    local skills=()
    for dir in "$PACKAGES_DIR"/*/; do
        dir=$(basename "${dir%/}")  # Get just the directory name
        if [ -f "$PACKAGES_DIR/$dir/SKILL.md" ]; then
            skills+=("$dir")
        fi
    done
    echo "${skills[@]}"
}

# List all available skills
list_skills() {
    echo -e "${BLUE}Available Skills:${NC}"
    echo ""

    local skills=($(find_skills))
    for skill in "${skills[@]}"; do
        local has_setup=""
        if [ -f "$PACKAGES_DIR/$skill/setup.sh" ]; then
            has_setup=" ${GREEN}[setup]${NC}"
        fi
        echo -e "  • ${YELLOW}$skill${NC}$has_setup"
    done

    echo ""
    echo -e "Total: ${GREEN}${#skills[@]}${NC} skills"
}

# Create IDE directory if it doesn't exist
ensure_directory() {
    local dir=$1
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo -e "${GREEN}✓${NC} Created $dir"
    fi
}

# Deploy skill to target directory
deploy_skill() {
    local skill=$1
    local target_dir=$2
    local skill_target="$target_dir/$skill"
    local skill_source="$PACKAGES_DIR/$skill"

    # Remove existing symlink or directory
    if [ -L "$skill_target" ] || [ -d "$skill_target" ]; then
        rm -rf "$skill_target"
    fi

    if [ "$DEPLOY_MODE" = "symlink" ]; then
        # Create relative symlink
        local relative_path="../../packages/$skill"
        ln -s "$relative_path" "$skill_target"
        echo -e "  ${GREEN}→${NC} Symlinked $skill"
    else
        # Copy directory
        cp -R "$skill_source" "$skill_target"
        echo -e "  ${GREEN}✓${NC} Copied $skill"
    fi
}

# Run setup script for a skill
run_skill_setup() {
    local skill=$1
    local setup_script="$PACKAGES_DIR/$skill/setup.sh"

    if [ -f "$setup_script" ]; then
        echo -e "  ${BLUE}⚙${NC}  Running setup for $skill..."
        (cd "$PACKAGES_DIR/$skill" && bash setup.sh)
        echo -e "  ${GREEN}✓${NC} Setup complete for $skill"
    fi
}

# Deploy to specific IDE
deploy_to_ide() {
    local ide_name=$1
    local ide_dir=$2

    echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Deploying to $ide_name${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    ensure_directory "$ide_dir"

    local skills=($(find_skills))
    local deployed=0

    for skill in "${skills[@]}"; do
        deploy_skill "$skill" "$ide_dir"

        # Run setup if requested
        if [ "$RUN_SETUP" = true ]; then
            run_skill_setup "$skill"
        fi

        ((deployed++))
    done

    echo -e "\n${GREEN}✓${NC} Deployed ${GREEN}$deployed${NC} skills to $ide_name ($ide_dir)"
}

# Clean up all IDE deployments
clean_deployments() {
    echo -e "${YELLOW}Cleaning up IDE deployments...${NC}\n"

    local dirs=("$CLAUDE_DIR" "$CURSOR_DIR" "$GITHUB_DIR")
    for dir in "${dirs[@]}"; do
        if [ -d "$dir" ]; then
            rm -rf "$dir"
            echo -e "${GREEN}✓${NC} Removed $dir"
        fi
    done

    echo -e "\n${GREEN}✓${NC} Cleanup complete"
}

# Validate Python is available for validation (optional)
check_validation_tools() {
    if command -v python3 &> /dev/null; then
        local validator="$PACKAGES_DIR/skill-creator/scripts/quick_validate.py"
        if [ -f "$validator" ]; then
            return 0
        fi
    fi
    return 1
}

# Main execution
main() {
    parse_args "$@"

    echo -e "${BLUE}╔═══════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║   A11y Skills Deployment Tool        ║${NC}"
    echo -e "${BLUE}╚═══════════════════════════════════════╝${NC}"

    echo -e "\nMode: ${YELLOW}$DEPLOY_MODE${NC}"
    if [ "$RUN_SETUP" = true ]; then
        echo -e "Setup: ${GREEN}enabled${NC}"
    fi

    # Deploy to selected IDEs
    if [ "$DEPLOY_CLAUDE" = true ]; then
        deploy_to_ide "Claude Code" "$CLAUDE_DIR"
    fi

    if [ "$DEPLOY_CURSOR" = true ]; then
        deploy_to_ide "Cursor" "$CURSOR_DIR"
    fi

    if [ "$DEPLOY_GITHUB" = true ]; then
        deploy_to_ide "GitHub Copilot" "$GITHUB_DIR"
    fi

    # Summary
    echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}✓ Deployment complete!${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

    # Show deployed locations
    echo -e "Skills deployed to:"
    if [ "$DEPLOY_CLAUDE" = true ]; then
        echo -e "  • ${YELLOW}$CLAUDE_DIR${NC}"
    fi
    if [ "$DEPLOY_CURSOR" = true ]; then
        echo -e "  • ${YELLOW}$CURSOR_DIR${NC}"
    fi
    if [ "$DEPLOY_GITHUB" = true ]; then
        echo -e "  • ${YELLOW}$GITHUB_DIR${NC}"
    fi

    echo ""

    # Reminder about setup
    if [ "$RUN_SETUP" = false ]; then
        local has_setup_skills=false
        local skills=($(find_skills))
        for skill in "${skills[@]}"; do
            if [ -f "$PACKAGES_DIR/$skill/setup.sh" ]; then
                has_setup_skills=true
                break
            fi
        done

        if [ "$has_setup_skills" = true ]; then
            echo -e "${YELLOW}Note:${NC} Some skills have setup.sh scripts for downloading external resources."
            echo -e "      Run with ${YELLOW}--setup${NC} flag to execute them automatically."
            echo ""
        fi
    fi
}

# Run main function
main "$@"
