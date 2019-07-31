#!/usr/bin/env python3


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def test(l):
    primes = []
    i = 1
    n = 2

    while i <= l:
        if is_prime(n):
            primes.append(n)
            i += 1
        
        n += 1

    return primes


if __name__ == '__main__':
    result = test(20)
    print(result)
