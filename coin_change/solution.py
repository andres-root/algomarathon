#!/usr/bin/env python3



def coin_change_first(cents):
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

def coin_change(target):
    if target < 1:
        return 0

    solutions = []
    coins = [25, 10, 1]
    i = 0

    while i <= len(coins) - 1:
        num_of_coins = 0
        cents = target

        for j in range(i, len(coins) + 1):
            coin = coins[j]
            num_of_coins += cents // coin
            cents = cents % coin

            if len(solutions) > 0 and num_of_coins >= solutions[len(solutions) - 1]:
                break

            if cents == 0:
                solutions.append(num_of_coins)
                break
        i += 1
    
    return min(solutions)
        
change = coin_change(70)
print(change)
