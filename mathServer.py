from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """this tool is responsible for adding two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """this tool is responsible for subtracting two numbers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """this tool is responsible for multiplying two numbers"""
    return a * b

""" if i specify the transport is stdion then then it will teels the server to:
    Use the standard input and output streams for communication with the client
    This is basically used for testing and debugging
    It uses basically terminal for getting the input and the output
    Lets say if i give any input then it should go throught the command line hit any function and then get the output from that function
"""

if __name__ == "__main__":
    print("MathServer is starting...")
    mcp.run(transport =  "stdio")