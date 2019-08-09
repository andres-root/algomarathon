#!/usr/bin/env python3



def common_bf(arr1, arr2):
    common = []

    for e in arr2:
        if e in arr1:
            common.append(e)
    
    return common

def common_ht(arr1, arr2):
    ht = {}
    common = []

    for e in arr1:
        try:
            ht[e] += 1
        except KeyError:
            ht[e] = 1
        
        if ht[e] > 1:
            common.append(ht[e])

    for e in arr2:
        try:
            ht[e] += 1
        except KeyError:
            ht[e] = 0
        
        if ht[e] > 1:
            common.append(e)

    print(ht)
    return common
            

arr1 = [1, 5, 12, 3, -15, 52]
arr2 = [3, 1, 6, 5, 57, 13, 17]
common_bf = common_bf(arr1, arr2)
common_ht = common_ht(arr1, arr2)
print(common_bf, common_ht)
