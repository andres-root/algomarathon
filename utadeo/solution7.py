#!/usr/bin/env python3

series = []

def fibonacci(n, mem={}):
    if n in mem.keys():
        return mem[n]

    if n == 1 or n == 2:
        fib = 1
    else:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
    
    mem[n] = fib
    series.append(fib)

    return fib

def test(test_cases):
    results = []

    for n in test_cases:
        fibonacci(n)
        results.append(series)

    return results


if __name__ == '__main__':
    test_cases = [10]
    print(list(zip(test_cases, test(test_cases))))
