#!/usr/bin/env python3

def insertion_sort(numbers):
    for j in range(1, len(numbers)):
        key = numbers[j]  # 2
        i = j - 1

        while i >= 0 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            i -= 1
        
        numbers[i + 1] = key
    
    return numbers


if __name__ == '__main__':
    numbers = [5, 2, 4, 6, 1, 3]
    sorted_numbers = insertion_sort(numbers)
    print(sorted_numbers)