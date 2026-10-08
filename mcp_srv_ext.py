from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DemoSrvExt")
print("Starting Ext FastMCP server...")

@mcp.tool()
def subtrack(a: int, b: int) -> int:
    """Subtract two integers"""
    print("Subtracting two integers...")
    return a - b
