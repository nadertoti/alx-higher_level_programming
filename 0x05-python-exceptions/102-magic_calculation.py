#!/usr/bin/python3
def magic_calculation(a, b):
    value = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            value += a ** b / j
        except Exception:
            value = b + a
            break
    return value
