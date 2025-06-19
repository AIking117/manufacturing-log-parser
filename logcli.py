#!/usr/bin/env python3
import os
import sys
import argparse
import json
import csv
import io
from manufacturelog import validate_and_extract_log

parser = argparse.ArgumentParser(description="Parse manufacturing logs into structured batches")
parser.add_argument("input", help="Path to log file or raw log string")
parser.add_argument("-o", "--output", choices=["json","csv"], default="json", help="Output format")
parser.add_argument("-f", "--outfile", help="Filename to write results to (defaults to stdout)")

if __name__ == "__main__":
    args = parser.parse_args()

    if os.path.isfile(args.input):
        with open(args.input, 'r') as fh:
            log_string = fh.read().strip()
    else:
        log_string = args.input

    result = validate_and_extract_log(log_string)
    if result == "invalid":
        sys.exit("Error: the provided log string is invalid.")

    if args.output == "json":
        serialized = json.dumps(result, indent=2)
    else:
        keys = result[0].keys()
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=keys)
        writer.writeheader()
        writer.writerows(result)
        serialized = buffer.getvalue()

    if args.outfile:
        with open(args.outfile, "w") as out_fh:
            out_fh.write(serialized)
    else:
        print(serialized)
