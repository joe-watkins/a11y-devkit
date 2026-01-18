# Next Steps: Phase 2 - Update a11y-devkit-deploy

After Phase 1 (monorepo setup) is complete, Phase 2 requires updates to the `a11y-devkit-deploy` repository:

## Phase 2 Tasks

### 1. Update `config/a11y.json`

Replace git repository reference with npm package list:

```json
{
  "skills": [
    "a11y-base-web-skill",
    "a11y-issue-writer-skill",
    "a11y-tester-skill",
    "a11y-remediator-skill",
    "a11y-validator-skill",
    "web-standards-skill",
    "a11y-audit-fix-agent-orchestrator-skill"
  ]
}
```

### 2. Rewrite `src/installers/skills.js`

New npm-based installer that:

1. Creates temp directory with package.json listing skills as dependencies
2. Runs `npm install` in temp directory
3. Copies installed packages to IDE skills directories
4. Cleans up temp directory

### 3. Update `src/cli.js`

- Remove git clone workflow
- Call new `installSkillsFromNpm()` function
- Update user messaging

### 4. Delete `src/installers/repo.js`

Git clone logic no longer needed

### 5. Bump Version

Update `package.json` version to `0.6.0`

### 6. Update `README.md`

Document new npm-based installation approach

## Publishing Workflow

```bash
# In a11y-devkit (after Phase 2 complete)
npm version patch --workspaces
npm publish --workspaces --access public

# In a11y-devkit-deploy (after skills published)
npm version minor
npm publish
```

## Verification Checklist

- [ ] Skills install via npm (not git)
- [ ] Skills appear in `.claude/skills/`, `.cursor/skills/`, etc.
- [ ] All 8 skills load properly in IDE
- [ ] CLI tool runs without errors
