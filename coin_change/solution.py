#!/usr/bin/env python3



def coin_change(cents):
    if cents < 1:
        return 0
    
    available_coins = {
        25: 25,
        10: 10,
        5: 5,
        1: 1,
    }
    
    if cents in available_coins.keys():
        return available_coins[cents]

    i = 0
    coins = []
    arr = list(available_coins.keys())
    c = 0
    while i <= len(arr) - 1:
        c += 1
        print(c)
        coin = arr[i]

        if cents == 0:
            return coins
        
        if cents >= coin:
            cents -= coin
            coins.append(coin)
        else:
            i += 1
    return coins
        
change = coin_change(31)
print(len(change), change)
