from mcp.server.fastmcp import FastMCP
mcp = FastMCP('Python-MCP-Server')
@mcp.tool()
def get_info_about(name : str) -> str:
    """
    Get Information about a given employee name:
    - Name
    - Salary
    - Email
    """
    return {
        "name" :"Nacera",
        "salary":50000,
        "email":"nossanacera@gmail.com"
    }
