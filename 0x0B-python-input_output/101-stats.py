#!/usr/bin/python3

"""Log parsing and using a default dict to count
values to get a default
"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_code_counts):
    """Print Statistics"""
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")


def process_input_line(line, total_size, status_code_counts):
    """Process in put line"""
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += size
        status_code_counts[status_code] += 1

    except (ValueError, IndexError):
        # Ignore lines that don't match the expected format
        pass

    return total_size, status_code_counts


def main():
    """main function"""
    total_size = 0
    status_code_counts = defaultdict(int)
    line_counter = 0

    try:
        for line in sys.stdin:
            total_size, status_code_counts = process_input_line(
                line, total_size, status_code_counts)
            line_counter += 1

            if line_counter % 10 == 0:
                print_statistics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle CTRL+C interruption
        print_statistics(total_size, status_code_counts)


if __name__ == "__main__":
    main()
