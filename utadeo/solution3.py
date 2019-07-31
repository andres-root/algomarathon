#!/usr/bin/env python3


def is_palindrome(w):
    if len(w) <= 2:
        return True

    if w[0] == w[len(w) - 1]:
        return is_palindrome(w[1:-1])
    else:
        return False

def test(arr):
    return [is_palindrome(w) for w in arr]


if __name__ == '__main__':
    arr = ['anna', 'andres', 'tadeo', 'civic', 'kayak', 'linux', 'madam', 'dog', 'mom', 'cat', 'radar']
    print(list(zip(arr, test(arr))))
