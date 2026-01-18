from fastmcp import FastMCP
import random 
import json


# create FastMCP instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# Tool: Generate a random number within a range
@mcp.tool
def generate_random_number(min_value: int, max_value: int) -> int:
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

# Resource: Server Information 
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A server that provides basic calculator functions and random number generation.",
        "tools": ["add", "generate_random_number"],
        "author": ["Varsha Dewangan"]
    }

    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)