#!/usr/bin/python3

import sys
import urllib.request

if __name__ == "__main__":
    text = sys.argv[1]

    request = urllib.request.Request(text)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
