class BaseTool:
    @staticmethod
    def tool_info():
        raise NotImplementedError

    @staticmethod
    def handler(params):
        raise NotImplementedError
