from mcp.core.transport import read_message, send_message
from mcp.core.dispatcher import Dispatcher
from mcp.tools.ping import ping

def main():
    dispatcher = Dispatcher(tools=[ping])

    while True:
        req = read_message()
        if req is None:  # stdin closed
            break
        response = dispatcher.handle(req)
        if response:
            send_message(response)

if __name__ == "__main__":
    main()
