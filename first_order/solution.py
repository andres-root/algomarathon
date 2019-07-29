#!/usr/bin/env python3


def single_min(numbers):
    min_value = numbers[0]

    for n in numbers:
        if n < min_value:
            min_value = n
    
    return min_value


def pair_min(numbers):
    min_values = [numbers[0], numbers[1]]

    for n in numbers:
        if n < min_values[0]:
            min_values[1] = min_values[0]
            min_values[0] = n
        elif n < min_values[1] and n > min_values[0]:
            min_values[1] = n

    return min_values


def kmin(numbers, k):
    # [8, 1, 10, 5, 7, 2, 14, 3, 6, 16, 4, 20, 15, 12, 13, 0, 11, 9, 19, 18, 16]
    j = 0
    c = 1
    while c <  len(numbers):
        for i in range(c, len(numbers)):
            if numbers[j] > numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
                j = i
        c += 1

    return numbers

if __name__ == '__main__':
    # numbers = [5, 4, 10, 12, 23, 37, 32, 44, 35, 109, 99, 111, 98]
    # numbers = [2, 2, 3, 3, 2, 5, 6]
    numbers = [8, 1, 10, 5, 7, 18, 2, 14, 3, 6, 17, 16, 4, 20, 15, 12, 13, 0, 11, 9, 19]

    result = kmin(numbers, 10)
    print(result)
