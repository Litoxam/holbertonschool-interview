#!/usr/bin/python3
"""
Reads stdin and computes metrics.
"""

import sys
import re

pattern = re.compile(
    r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\S+) (\S+)$'
)

VALID_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_stats(total_size, status_codes):
    """Print metrics."""
    print("File size: {}".format(total_size))

    for code in VALID_CODES:
        if code in status_codes:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1

            match = pattern.fullmatch(line.strip())

            if match:
                status = match.group(1)
                size = int(match.group(2))

                total_size += size

                if status in VALID_CODES:
                    if status in status_codes:
                        status_codes[status] += 1
                    else:
                        status_codes[status] = 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
