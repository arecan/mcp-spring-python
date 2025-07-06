from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP('Python-MCP-Server')

@mcp.tool()
def get_info_about(name: str) -> str:
    """
    Get information about a given employee name:
    - Name
    - Salary
    - Email
    """
    employee_info = {
        "name": "Nacera",
        "salary": 50000,
        "email": "nossanacera@gmail.com"
    }
    return json.dumps(employee_info)