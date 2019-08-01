#!/usr/bin/env python3


def merge(l, r):
    m = []
    li = 0
    ri = 0

    while li < len(l) and ri < len(r):
        if l[li] > r[ri]:
            m.append(r[ri])
            ri += 1
        else:
            m.append(l[li])
            li += 1

    m += l[li:]
    m += r[ri:]

    return m

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr)//2
    
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    return merge(l, r)


def test_function(test_cases):
    results = []

    for arr in test_cases:
        results.append(merge_sort(arr))
    
    return results


if __name__ == '__main__':
    arr = [2, 5, 7, 3, 1, 8, 9]
    test_cases = [arr]
    print(test_function(test_cases))
