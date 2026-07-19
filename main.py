from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def random_number(min: int = 1, max: int = 100) -> int:
    """Generate a random number between min and max."""
    return random.randint(min, max)

@mcp.resource("info://server")
def server_info() -> str:
    """Return server information."""
    return json.dumps({
        "name": mcp.name,
        "version": mcp.version,
        "description": "A basic mcp server with simple tools and resources.",
        "tools": ["add", "random_number"],
        "author": "Ajendra Singh",
    }, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)