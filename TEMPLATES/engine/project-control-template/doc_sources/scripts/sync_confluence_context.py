#!/usr/bin/env python3
import subprocess, sys
if __name__ == "__main__":
    raise SystemExit(subprocess.call([sys.executable, __file__.replace("sync_confluence_context.py","fetch_confluence.py")] + sys.argv[1:]))
