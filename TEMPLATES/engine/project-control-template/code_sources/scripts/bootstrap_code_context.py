#!/usr/bin/env python3
import argparse
from code_context_runtime import build_context
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--target", default="."); ap.add_argument("--source", default="backend-main"); ap.add_argument("--path", default="backend")
    a=ap.parse_args(); print(build_context(a.target,a.source,a.path))
if __name__=="__main__": main()
