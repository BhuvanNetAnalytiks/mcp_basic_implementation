from mcp.server.fastmcp import FastMCP
import random
from bs4 import BeautifulSoup

mcp = FastMCP("WeatherServer")

@mcp.tool()
async def get_temperature(city: str) -> float:
    """this tool is responsible for getting the temepearture fo the particular city"""
    return float(random.randint(10,25))

# when i run the particular file as streamable http then it will start the server and then it will litsen to the request coming from the 
# client and then it will give the output
if __name__ == "__main__":
    print("WeatherServer is starting...")
    mcp.run(transport = "streamable-http")