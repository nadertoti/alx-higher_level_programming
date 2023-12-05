#!/usr/bin/python3
"""script that reads stdin line"""


from sys import stdin


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
    }

total_size = i = 0

def spliter():
    """function prints the status in statistical form."""
    print(f'File size: <total size>')
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))

try:
    for line in stdin:
        splitted_line = line.split()
        if len(splitted_line) >= 2:
            status = splitted_line[-2]
            total_size += int(splitted_line[-1])
            if status in status_codes:
                status_codes[status] += 1
        i += 1

        if i % 10 == 0:
            spliter()
    spliter()
except KeyboardInterrupt as e:
    spliter()
