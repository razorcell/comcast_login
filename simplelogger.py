class SimpleLogger:
    def info(self, msg: str):
        print(f"INFO: {msg}")

    def warning(self, msg: str):
        print(f"WARNING: {msg}")

    def error(self, msg: str):
        print(f"ERROR: {msg}")