#!/usr/bin/env python3


def power_of_two(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    
    return power_of_two(n/2)

def test(arr):
    return [power_of_two(n) for n in arr]


if __name__ == '__main__':
    arr = [x for x in range(1, 11)]
    print(list(zip(arr, test(arr))))
