# FastMCP Data Server Creator

## Overview
A specialized skill for rapidly creating Model Context Protocol (MCP) servers using FastMCP 2.0 to expose structured data (JSON, markdown, CSV, etc.) through standardized tools. Optimized for deployment to FastMCP Cloud.

## When to Use This Skill
- User has a data file or collection of data files (JSON, markdown, CSV, etc.)
- User wants to expose data through an MCP server for AI assistants
- User needs quick deployment to FastMCP Cloud
- User wants standardized query tools for their data
- Project involves creating a data API accessible by Claude, Cursor, or other MCP clients

## Core Competencies
1. **Data File Analysis** - Inspect and understand data structure from various formats
2. **FastMCP Server Creation** - Build optimized server.py with appropriate tools
3. **Tool Design** - Create intuitive, data-appropriate MCP tools (search, get by ID, random, range queries)
4. **Dependency Management** - Generate minimal requirements.txt
5. **Testing & Validation** - Create test scripts and verify functionality
6. **Cloud Deployment Prep** - Ensure compatibility with FastMCP Cloud requirements
7. **Documentation** - Generate comprehensive README with deployment instructions

## Typical Workflow

### 1. Data Discovery & Analysis
```bash
# Identify data files in the workspace
- Look for /data, /content, or similar folders
- Identify file formats (JSON, markdown, CSV, YAML, etc.)
- Understand data structure and access patterns
- Determine appropriate query methods
```

### 2. Server Creation
```python
# Create server.py with FastMCP 2.0
from fastmcp import FastMCP
import json
from pathlib import Path

mcp = FastMCP("Server Name")

# Load data
DATA_PATH = Path(__file__).parent / "data" / "datafile.json"

@mcp.tool()
def tool_name(param: type) -> str:
    """Tool description"""
    # Implementation
    pass
```

### 3. Essential Tools to Create
Based on data type, implement relevant tools:

**For ID-based records (JSON arrays with IDs):**
- `get_by_id(id)` - Retrieve specific item
- `search(keyword)` - Search across text fields
- `get_random()` - Random item
- `get_count()` - Total count
- `get_by_range(start, end)` - Range query
- `list_all()` - Complete dataset (if reasonable size)

**For markdown/text collections:**
- `search_content(keyword)` - Search across files
- `get_file(filename)` - Get specific file
- `list_files()` - Directory listing
- `get_random_file()` - Random selection

**For tabular data (CSV):**
- `query_by_column(column, value)` - Filter by column
- `get_columns()` - Schema information
- `get_stats()` - Data statistics

### 4. Project Structure
```
project-root/
├── server.py              # Main FastMCP server
├── requirements.txt       # Dependencies (minimal)
├── README.md             # Documentation + deployment guide
├── test_server.py        # Validation script
└── data/                 # Data files
    └── datafile.json
```

### 5. Testing Approach
Create `test_server.py` to validate:
- Data loads correctly
- All query patterns work
- Edge cases handled (not found, invalid ranges, etc.)
- No MCP tool wrapper issues

### 6. FastMCP Cloud Requirements Checklist
- ✓ Single `server.py` file with FastMCP instance
- ✓ Server object clearly defined (e.g., `mcp = FastMCP(...)`)
- ✓ `requirements.txt` with `fastmcp>=2.0.0`
- ✓ Data files in repository
- ✓ Relative path resolution using `Path(__file__).parent`
- ✓ No external dependencies required at runtime
- ✓ Tools have clear docstrings
- ✓ Type hints on all parameters and returns

### 7. Documentation Template
README.md should include:
- Server description
- List of available tools with examples
- Local installation steps
- FastMCP Cloud deployment instructions (with entrypoint)
- Usage examples for MCP clients
- Data source attribution

## Key Patterns & Best Practices

### Data Loading
```python
# Use Path for cross-platform compatibility
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "file.json"

def load_data():
    """Load data at module level for efficiency"""
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

DATA = load_data()  # Load once
```

### Tool Design
```python
@mcp.tool()
def search_items(keyword: str) -> str:
    """
    Search for items containing a keyword.
    
    Args:
        keyword: The search term
    
    Returns:
        Formatted results or "not found" message
    """
    keyword_lower = keyword.lower()
    matches = [item for item in DATA if keyword_lower in str(item).lower()]
    
    if not matches:
        return f"No items found containing '{keyword}'"
    
    # Return formatted, readable results
    result = f"Found {len(matches)} item(s):\n\n"
    for item in matches:
        result += f"- {format_item(item)}\n"
    
    return result.strip()
```

### Error Handling
```python
@mcp.tool()
def get_item(item_id: int) -> str:
    """Get item by ID with proper error handling"""
    item = next((i for i in DATA if i['id'] == item_id), None)
    
    if not item:
        return f"Item #{item_id} not found. Valid IDs: 1-{len(DATA)}"
    
    return f"Item #{item['id']}: {item['content']}"
```

### Requirements Management
```txt
# Minimal requirements.txt
fastmcp>=2.0.0

# Add only if needed:
# pandas>=2.0.0  # For CSV/Excel
# pyyaml>=6.0    # For YAML files
# markdown>=3.0  # For markdown processing
```

## Common Data Patterns

### JSON Array with IDs
```json
{
  "items": [
    {"id": 1, "name": "Item 1", "description": "..."},
    {"id": 2, "name": "Item 2", "description": "..."}
  ]
}
```
**Tools**: get_by_id, search, get_random, get_range, get_count

### Markdown Collection
```
data/
├── item-1.md
├── item-2.md
└── item-3.md
```
**Tools**: get_file, search_content, list_files, get_random_file

### CSV/Tabular
```csv
id,name,category,value
1,Item A,Cat1,100
2,Item B,Cat2,200
```
**Tools**: query_by_column, filter_by_category, get_stats, export_filtered

## FastMCP Cloud Deployment Instructions

### Prerequisites
- GitHub account
- GitHub repository containing:
  - `server.py` with FastMCP server instance
  - `requirements.txt` with dependencies
  - Data files (JSON, markdown, etc.)

### Step-by-Step Deployment

**Step 1: Visit FastMCP Cloud**
1. Navigate to [fastmcp.cloud](https://fastmcp.cloud/)
2. Sign in with your GitHub account

**Step 2: Create a Project**
1. Click "Create a Project"
2. Choose your GitHub repository (can be public or private)
3. Configure the deployment:
   - **Name**: Choose a unique name (creates URL: `https://your-name.fastmcp.app/mcp`)
   - **Entrypoint**: `server.py:mcp` (format: `filename.py:object_name`)
   - **Authentication**: 
     - Disabled = Public access
     - Enabled = Organization members only
4. Click "Deploy"

**Step 3: Automatic Build & Deploy**
FastMCP Cloud will automatically:
- Clone your repository
- Detect dependencies from `requirements.txt` or `pyproject.toml`
- Install Python packages
- Build and deploy your server
- Provide a unique URL for connections

**Step 4: Connect to Your Server**
Once deployed, your server is available at:
```
https://your-project-name.fastmcp.app/mcp
```

FastMCP Cloud provides instant connection configs for:
- **Claude Desktop** - Copy/paste JSON config
- **Cursor** - Connection settings
- **Any MCP Client** - Use the provided URL

**Step 5: Auto-Updates**
- FastMCP Cloud monitors your `main` branch
- Automatic redeployment on every push
- PR builds get unique URLs for testing before production

### Pre-Deployment Validation
```bash
# Verify your server is compatible
fastmcp inspect server.py:mcp

# Test locally first
python server.py
```

### Deployment Checklist
- [ ] Repository is on GitHub (public or private)
- [ ] `server.py` contains FastMCP instance (e.g., `mcp = FastMCP(...)`)
- [ ] `requirements.txt` includes `fastmcp>=2.0.0` and all dependencies
- [ ] Data files are in the repository
- [ ] Server uses relative paths (`Path(__file__).parent`)
- [ ] All tools have docstrings and type hints
- [ ] Server runs locally without errors
- [ ] No external API keys or services required (unless using secrets)

### Common Configuration Patterns

**Basic Entrypoint:**
```python
# server.py
from fastmcp import FastMCP
mcp = FastMCP("My Server")

# Entrypoint: server.py:mcp
```

**Named Server:**
```python
# app.py
from fastmcp import FastMCP
my_app = FastMCP("Data Service")

# Entrypoint: app.py:my_app
```

**Module Structure:**
```python
# src/main.py
from fastmcp import FastMCP
server = FastMCP("Service")

# Entrypoint: src/main.py:server
```

### Troubleshooting

**Build Failures:**
- Check `requirements.txt` syntax
- Ensure all imports are in requirements
- Verify Python version compatibility (3.8+)

**Runtime Errors:**
- Check data file paths (use relative paths)
- Verify data files exist in repository
- Review server logs in FastMCP Cloud dashboard

**Connection Issues:**
- Confirm deployment succeeded
- Check authentication settings
- Verify URL format includes `/mcp` endpoint

### Documentation Template for README

```markdown
## Deployment to FastMCP Cloud

### Quick Start
1. Visit [fastmcp.cloud](https://fastmcp.cloud/) and sign in with GitHub
2. Create new project from this repository
3. Configure:
   - **Name**: `your-project-name`
   - **Entrypoint**: `server.py:mcp`
   - **Authentication**: Choose public or private
4. Deploy (automatic)
5. Connect at: `https://your-project-name.fastmcp.app/mcp`

### Verify Before Deployment
```bash
fastmcp inspect server.py:mcp
```

### Auto-Updates
Push to `main` branch to automatically redeploy. PR builds get unique testing URLs.
```

## Testing Checklist
Before deployment:
- [ ] Data loads successfully
- [ ] All tools return properly formatted strings
- [ ] No circular imports or tool wrapper issues
- [ ] Edge cases handled (not found, invalid params)
- [ ] `requirements.txt` includes all dependencies
- [ ] README includes deployment instructions
- [ ] Server runs without errors: `python server.py`
- [ ] Test script validates core functionality

## Common Pitfalls to Avoid

1. **Tool Return Types** - Always return `str`, not objects
2. **Tool Decorator Issues** - Don't call decorated tools directly in tests
3. **Path Resolution** - Use `Path(__file__).parent` not `os.getcwd()`
4. **Large Datasets** - Consider pagination or summaries for >1000 items
5. **External APIs** - FastMCP Cloud needs self-contained data
6. **Missing Encoding** - Always use `encoding='utf-8'` when reading files
7. **Hardcoded Paths** - Use relative paths from project root
8. **If __name__ Blocks** - Optional; ignored by FastMCP Cloud

## Example Output Structure

For this Ferengi Rules example:
- ✅ 6 tools created (get_rule, search_rules, get_random_rule, list_all_rules, get_rules_count, get_rules_by_range)
- ✅ Data loads 286 JSON records
- ✅ Comprehensive search functionality
- ✅ Range queries with validation
- ✅ Test script validates all patterns
- ✅ README with deployment guide
- ✅ Ready for FastMCP Cloud deployment

## Success Criteria
- Server loads without errors
- All tools return formatted, helpful responses
- Data is accessible through intuitive query patterns
- Documentation enables self-service deployment
- Tests validate core functionality
- Compatible with FastMCP Cloud requirements
- Deployable in < 5 minutes to production

## Related Technologies
- **FastMCP 2.0** - Core framework
- **Model Context Protocol** - MCP specification
- **FastMCP Cloud** - Managed hosting platform
- **Python 3.8+** - Runtime environment
- **JSON/YAML/CSV** - Common data formats

## Version History
- v1.0 - Initial skill for FastMCP 2.0 data server creation
