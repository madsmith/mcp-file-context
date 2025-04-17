# MCP File Context

A FastMCP server that provides access to files within the .venv directory that are typically not accessible due to .gitignore rules. This enables AI agents to inspect implementation details of installed packages, improving their ability to understand and work with dependencies.

## Overview
This project demonstrates how to build an MCP server that enables AI agents to read files from within the .venv directory. It serves as both a practical tool and a template for creating your own MCP servers.

The implementation follows the best practices laid out by Anthropic for building MCP servers, allowing seamless integration with any MCP-compatible client.

## Features
The server provides one essential file access tool:
- `get_file_contents`: Read the contents of a file from within the .venv directory, enabling access to implementation details of installed packages

## Prerequisites
- Python 3.12+
- uv package manager

## Installation

### Using uv
1. Install uv if you don't have it:
```bash
pip install uv
```

2. Clone this repository:
```bash
git clone https://github.com/yourusername/mcp-file-context.git
cd mcp-file-context
```

3. Install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

## Running the Server

### Using stdio mode (default)
Run the server in stdio mode (recommended for local development):
```bash
mcp-file-context
```

### Using SSE mode
Run the server in SSE mode:
```bash
mcp-file-context --server
```

By default, the server runs on port 8050. You can configure the host and port using the `-H` and `-p` flags respectively.

## Integration with MCP Clients

### Python with Stdio Configuration
The server automatically registers itself with Cascade when installed in editable mode (`pip install -e .`). No additional configuration is needed.

### SSE Configuration
If running in SSE mode, configure your MCP client to connect to:
```
http://localhost:8050
```

## Usage Example
```python
# Reading a package's implementation file
contents = get_file_contents("lib/python3.13/site-packages/fastmcp/__init__.py")
```

## About

### License
MIT

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
