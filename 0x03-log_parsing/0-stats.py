#!/usr/bin/python3
"""Log parsing"""
import sys

possible_status_codes = [100, 301, 400, 401, 403, 404, 405, 500]
totalFileSize = 0
numberOfLines = 0
mapStatusCodes = {}


def print_stats():
    """A function that handles print"""
    print(f"File size: {totalFileSize}")

    for status, count in sorted(mapStatusCodes.items()):
        print(f"{status}: {count}")


try:
    for line in sys.stdin:
        try:
            fileSize = int(line.split(' ')[-1])
            totalFileSize += fileSize
            statusCode = int(line.split(' ')[-2])

            if statusCode in possible_status_codes:
                if statusCode in mapStatusCodes:
                    mapStatusCodes[statusCode] += 1
                else:
                    mapStatusCodes[statusCode] = 1

            numberOfLines += 1

            if numberOfLines % 10 == 0:
                print_stats()
        except ValueError:
            pass

    if (numberOfLines == 0) or (numberOfLines % 10 != 0):
        print_stats()
except KeyboardInterrupt:
    print_stats()
