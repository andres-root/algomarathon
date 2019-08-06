#!/usr/bin/env python3

import time

def other_increment(arr, n=1):
    c = 1
    r = len(arr) - 1

    for i in range(r, -1, -1):
        s = arr[i] + c
        if s == 10:
            c = 1
        else:
            c = 0
        
        arr[i] = s % 10
    
    if c == 1:
        arr.insert(0, 1)
        

def increment(arr, n=1):
    if len(arr) == 0:
        return False

    if len(arr) == 1:
        return arr[0] + 1

    l = 0
    r = len(arr) - 1

    
    while True:
        if r < l:
            return arr

        if arr[r] == 9:
            arr[r] = 0
            
            if r == 0:
                arr.insert(0, 1)
                return arr
            else:
                r -= 1
        else:
            arr[r] += 1
            return arr

        
if __name__ == '__main__':
    arr = [9, 9, 0, 0]
    c = 0
    while True:
        if c == 11:
            break

        print(arr)
        time.sleep(1)
        other_increment(arr)
        # c += 1
