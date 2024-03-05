#!/usr/bin/python3

import sys
import requests


if __name__ == "__main__":
    text = sys.argv[1]

    result = requests.get(url)
    print(result.headers.get("X-Request-Id"))
