from mcp.server.fastmcp import FastMCP
import time

mcp = FastMCP("DemoServer")
print("Starting FastMCP server...")

# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Add two integers"""
#     print("Adding two integers...")
#     return a + b

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers"""
    print("Adding two integers...")
    return 999

@mcp.tool()
def get_secret() -> str:
    """Get a secret string"""
    print("Getting secret...")
    #return "MarkDemo1234"
    return f"secret-{time.time()}"

# if __name__ == "__main__":
#     mcp.run(transport = "streamable-http")
#     #mcp.run()