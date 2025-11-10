#!/usr/bin/env python
import argparse
from .client import ExvoClient

def main():
    parser = argparse.ArgumentParser(prog="exvo")
    parser.add_argument("--base", default="http://localhost:8000", help="Base URL for Exvo core")
    parser.add_argument("--list-assets", action="store_true", help="List assets")
    parser.add_argument("--snapshot", help="Get market snapshot for SYMBOL")
    args = parser.parse_args()

    client = ExvoClient(base_url=args.base)

    if args.list_assets:
        print(client.list_assets())
    if args.snapshot:
        print(client.get_snapshot(args.snapshot))

if __name__ == "__main__":
    main()
