import argparse
import asyncio
from pathlib import Path
from typing import Optional

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    "mcp-file-context",
    description="MCP server for reading .venv file contents"
)

# @mcp.resource("resource://.venv/{path}")
@mcp.tool()
def get_file_contents(path: str) -> Optional[str]:
    """Read the contents of a file from the .venv directory.
    
    This tool allows reading files from within the .venv directory that may be
    gitignored, enabling access to implementation details of installed packages.
    
    Args:
        path: The path to the file relative to the .venv directory
              (e.g. "lib/python3.9/site-packages/fastmcp/__init__.py")
        
    Returns:
        str: The contents of the file if found and readable
        None: If the file is not found, not accessible, or outside .venv
    
    Example:
        To read a package's __init__.py:
        >>> get_file_contents("lib/python3.9/site-packages/package/__init__.py")
    """
    venv_path = Path(".venv")
    target_path = venv_path / path
    
    try:
        # Ensure the path is within .venv directory
        if not target_path.resolve().is_relative_to(venv_path.resolve()):
            return None
            
        if target_path.is_file():
            return target_path.read_text()
        return None
    except (OSError, ValueError):
        return None

async def run_server(args: argparse.Namespace):
    """Run the MCP server with the specified arguments."""
    # Update server settings
    mcp.settings.host = args.host
    mcp.settings.port = args.port
    
    if args.server:
        # Run the MCP server with SSE transport
        await mcp.run_sse_async()
    else:
        # Run the MCP server with stdio transport
        await mcp.run_stdio_async()

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="MCP server for command and script execution"
    )
    parser.add_argument(
        "--server",
        action="store_true",
        help="Run in SSE server mode (default: stdio mode)"
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=8050,
        help="Port to run the server on (default: 8050)"
    )
    parser.add_argument(
        "-H", "--host",
        default="0.0.0.0",
        help="Host to run the server on (default: 0.0.0.0)"
    )
    return parser.parse_args()

def main():
    """Entry point for the MCP shell server."""
    args = parse_args()
    return asyncio.run(run_server(args))

if __name__ == "__main__":
    main()