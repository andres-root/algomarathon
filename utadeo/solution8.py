#!/usr/bin/env python3


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib = fibonacci(n - 1) + fibonacci(n - 2)
    arr.append(fib)
    
    return fib

def test(test_cases):
    results = []

    for n in test_cases:
        results.append(fibonacci(n))
    
    return results


if __name__ == '__main__':
    test_cases = [10]
    print(list(zip(test_cases, test(test_cases))))
