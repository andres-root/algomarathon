#!/usr/bin/env python3


def even(n):
    return (n % 2 == 0)

def test(numbers):
    for n in numbers:
        if even(n):
            print(n, 'even')
        else:
            print(n, 'odd')


if __name__ == '__main__':
    numbers = [x for x in range(1, 11)]
    test(numbers)
