from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathServer.py"],
                "transport": "stdio"
            },

            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable-http"
            } 
        }
    )

    import os

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    
    model = ChatGroq(model = "qwen/qwen3-32b")

    agent = create_agent(
        model,
        tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{
            "role": "user", 
            "content": "What is 10 * 45"
            }]
        }
    )

    print("Math Response: ", math_response["messages"][1])

asyncio.run(main())