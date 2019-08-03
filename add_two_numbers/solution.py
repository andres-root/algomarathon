#!/usr/bin/env python3


def add(l1, l2):
    n1 = ''.join([str(x) for x in l1])
    n2 = ''.join([str(x) for x in l2])
    
    n1 = int(n1[::-1])
    n2 = int(n2[::-1])
    
    r = str(n1 + n2)
    r = [int(x) for x in list(r)]
    return r[::-1]

if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(add(l1, l2))
