#!/usr/bin/env python3


def polydivisible(sn):
    n = int(sn)

    if len(sn) == 1:
        return True

    if not (n % len(sn) == 0):
        return False
    
    return polydivisible(sn[:len(sn) - 1])

def test(test_cases):
    results = []

    for n in test_cases:
        results.append(polydivisible(n))
    
    return results


if __name__ == '__main__':
    test_cases = ['381654729', '102', '9876', '1245553']
    print(list(zip(test_cases, test(test_cases))))
