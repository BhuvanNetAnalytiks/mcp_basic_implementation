The complete flow on how it works is like this:

                User
                  │
                  ▼
              create_agent
                  │
                  ▼
                 LLM
                  │
         "Call multiply tool"
                  │
                  ▼
             MCP Client
                  │
     Knows which server has multiply
                  │
                  ▼
          Math MCP Server
                  │
                  ▼
          multiply(10,45)
                  │
                  ▼
                450
                  │
                  ▼
             MCP Client
                  │
                  ▼
                Agent
                  │
                  ▼
                 LLM
                  │
                  ▼
            Final Answer