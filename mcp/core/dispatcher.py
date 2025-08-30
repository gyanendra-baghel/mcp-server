from mcp.core.protocol import make_response, make_error
from mcp.core import errors

class Dispatcher:
    def __init__(self, tools=[]):
        self.tools = {t.tool_info()["name"]: t for t in tools}

    def handle(self, req):
        method = req.get("method")
        req_id = req.get("id")

        print(f"Handling request: {req}")

        if method == "initialize":
            return make_response(req_id, {
                "name": "demo-mcp-server",
                "version": "0.1.0",
                "capabilities": {"tools": True}
            })

        elif method == "list_tools":
            tool_infos = [t.tool_info() for t in self.tools.values()]
            return make_response(req_id, tool_infos)

        elif method == "call_tool":
            params = req.get("params", {})
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})

            tool = self.tools.get(tool_name)
            if not tool:
                return make_error(req_id, errors.METHOD_NOT_FOUND, f"Unknown tool {tool_name}")

            result = tool.handler(tool_args)
            return make_response(req_id, result)

        else:
            return make_error(req_id, errors.METHOD_NOT_FOUND, f"Unknown method {method}")
