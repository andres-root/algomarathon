#!/usr/bin/env python3


def reverse(self, x: int) -> int:
    if x == 0:
        return 0

    x = str(x)[::-1]
    h = len(x) - 1
    
    if x[0] == '0':
        x = x[1:]
        h -= 1
    
    if x[h] == '-':
        sign = '-'
        x = '-{}'.format(x[:-1])
    x = int(x)
    
    if not (x <= (1 << 31) - 1) or not ((-1 << 31) <= x):
        return 0
    
    return x
