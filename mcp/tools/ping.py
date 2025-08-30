from mcp.tools.base import BaseTool
from mcp.tools.ping import ping
class PingTool(BaseTool):
    @staticmethod
    def tool_info():
        return {
            "name": "ping",
            "description": "Simple health check",
            "inputSchema": {"type": "object", "properties": {}}
        }

    @staticmethod
    def handler(params):
        return {"content": [{"type": "text", "text": "pong"}]}

# export instance
ping = PingTool()
