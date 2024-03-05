#!/usr/bin/python3

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    text = sys.argv[1]
    result = {"email": sys.argv[2]}
    argument = urllib.parse.urlencode(result).encode("ascii")

    request = urllib.request.Request(text, argument)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
