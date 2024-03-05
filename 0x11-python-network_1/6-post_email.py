#!/usr/bin/python3

import sys
import requests


if __name__ == "__main__":
    text = sys.argv[1]
    result = {"email": sys.argv[2]}

    argument = requests.post(text, data=result)
    print(argument.text)
