import sys

def log(msg):
    sys.stderr.write(f"[MCP] {msg}\n")
    sys.stderr.flush()
