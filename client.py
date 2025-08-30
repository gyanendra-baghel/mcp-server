import subprocess, json

def send_msg(proc, msg):
    proc.stdin.write(json.dumps(msg) + "\n")
    proc.stdin.flush()

def read_msg(proc):
    line = proc.stdout.readline()
    if not line:
        return None
    print("RESPONSE:", line.strip())
    return json.loads(line.strip())

def main():
    # Start the MCP server (adjust path if needed)
    proc = subprocess.Popen(
        ["python3", "server.py"],
        cwd=".",              # project root
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    # ---- 1. Initialize ----
    init_req = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
    send_msg(proc, init_req)
    print("INIT RESPONSE:", read_msg(proc))

    # ---- 2. List tools ----
    list_req = {"jsonrpc": "2.0", "id": 2, "method": "list_tools"}
    send_msg(proc, list_req)
    print("TOOLS RESPONSE:", read_msg(proc))

    # ---- 3. Call ping ----
    call_req = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "call_tool",
        "params": {"name": "ping", "arguments": {}}
    }
    send_msg(proc, call_req)
    print("PING RESPONSE:", read_msg(proc))

    proc.terminate()

if __name__ == "__main__":
    main()
