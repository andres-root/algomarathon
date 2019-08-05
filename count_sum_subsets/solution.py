#!/usr/bin/env python3


def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1)

def rec(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        return rec(arr, total, i - 1)
    else:
        return rec(arr, total - arr[i], i - 1) + rec(arr, total, i - 1)

def count_sets_dp(arr, total):
    mem = {}
    return dp(arr, total, len(arr) - 1, mem)

def dp(ar, total, i, mem):
    key = '{0}:{1}'.format(str(total), str(i))

    if key in mem.keys():
        return mem[key]
    
    if total == 0:
        result = 1
    elif total < 0:
        result = 0
    elif i < 0:
        result = 0
    elif total < arr[i]:
        result = dp(arr, total, i - 1, mem)
    else:
        result = dp(arr, total - arr[i], i - 1, mem) + dp(arr, total, i - 1, mem)
    
    mem[key] = result

    return result


def add_two_numbers_sets(arr, total):
    sums = {}
    sets = []
    r = len(arr) - 1
    i = 0
    
    while i <= r:
        d = total - arr[i]
        
        if d in sums.keys():
            sets.append((arr[sums[d]], arr[i]))
        else:
            sums[arr[i]] = i

        i += 1

    return sets


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # (6, 10+) (3, 5, 8) (1, 6, 9) (1, 2, 4, 9) (1, 2, 5, 8) (1, 7, 8) (2, 6, 8)
    total = 16
    result = add_two_numbers_sets(arr, total)
    print(len(result), result)
    print(count_sets(arr, total), count_sets_dp(arr, total))
