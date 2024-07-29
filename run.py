import sys
from entrypoints.console_app import start_app

if __name__ == "__main__":
    args = sys.argv[2:]
    param_to_start = int(sys.argv[1])
    start_app(param_to_start, args)