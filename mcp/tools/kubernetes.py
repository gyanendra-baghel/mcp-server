from mcp.tools.base import BaseTool

class KubernetesTool(BaseTool):
    @staticmethod
    def tool_info():
        return {
            "name": "list_pods",
            "description": "List pods in a namespace",
            "inputSchema": {
                "type": "object",
                "properties": {"namespace": {"type": "string"}},
                "required": ["namespace"]
            }
        }

    @staticmethod
    def handler(params):
        namespace = params.get("namespace", "default")
        # TODO: integrate kubernetes client
        return {"content": [{"type": "text", "text": f"Stub: pods in {namespace}"}]}

kubernetes = KubernetesTool()
