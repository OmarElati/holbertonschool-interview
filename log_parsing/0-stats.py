#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys
import re
from collections import defaultdict

pattern = r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

total_file_size = 0
status_code_counts = defaultdict(int)
lines_processed = 0

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            ip_address, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_file_size += file_size
            status_code_counts[status_code] += 1
            lines_processed += 1

            if lines_processed % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing current statistics:")
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
