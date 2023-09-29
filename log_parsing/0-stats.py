#!/usr/bin/python3
"""
Log Parsing Script

This script parses HTTP log lines from stdin and calculates statistics about the log data.

Usage:
- Input: Log lines are read from stdin, and they should follow a specific format.
- Output: The script prints the total file size and the count of each HTTP status code.

Log Line Format:
Each log line should have the format: IP_ADDRESS - [TIMESTAMP] "HTTP_REQUEST" STATUS_CODE FILE_SIZE

Example log line:
192.168.1.1 - [2023-09-29 15:30:45.123456] "GET /projects/260 HTTP/1.1" 200 12345

Note:
- Invalid log lines will be skipped.
- Invalid timestamps will be reported as errors.
"""

import sys
import re
from collections import defaultdict
from datetime import datetime


def parse_log_line(line, line_no, code_counts, total_file_size):
    pattern = r'(\S+) - \[(.*?)\] "(.*?)" (\d+) (\d+)'

    match = re.match(pattern, line)
    if match:
        ip, timestamp, request, status_code, file_size = match.groups()
        try:
            timestamp = timestamp.strip('[]')
            datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

            if request == 'GET /projects/260 HTTP/1.1':
                status_code = int(status_code)
                file_size = int(file_size)

                code_counts[status_code] += 1
                total_file_size += file_size

        except ValueError:
            sys.stderr.write(f"{sys.argv[0]}: {line_no}: Invalid timestamp\n")
            pass

    else:
        sys.stderr.write(f"{sys.argv[0]}: {line_no}: Invalid log line\n")

    return line_no, code_counts, total_file_size

def print_log_totals(total_file_size, code_counts):
    print("File size:", total_file_size)
    for code, count in code_counts.items():
        if count > 0:
            print(f"{code}: {count}")

if __name__ == '__main__':
    line_no = 0
    total_file_size = 0
    code_counts = defaultdict(int)

    try:
        for line in sys.stdin:
            line_no, code_counts, total_file_size = parse_log_line(
                line, line_no, code_counts, total_file_size)

            if line_no % 10 == 0:
                print_log_totals(total_file_size, code_counts)

        print_log_totals(total_file_size, code_counts)

    except KeyboardInterrupt:
        print_log_totals(total_file_size, code_counts)
        raise
