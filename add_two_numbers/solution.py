#!/usr/bin/env python3


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_number(node):
    number = ''

    while node:
        number += node.val
        node = node.next
    
    return number


def add(node1, node2):
    number1 = get_number(node2)
    number2 = get_number(node2)
    
    print(number1, number2)    


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    mem1 = None
    mem2 = None

    for i in range(len(l1)):
        node1 = Node(l1[i])
        node2 = Node(l2[i])

        if (mem1 and mem2):
            mem1.next = node1
            mem2.next = node2
        else:
            first1 = node1
            first2 = node2
        
        mem1 = node1
        mem2 = node2
    
    
    
    print(add(first1, first2))
