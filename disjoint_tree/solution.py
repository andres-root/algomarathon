#!/usr/bin/env python3
"""
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest.  You may return the result in any order.

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""

class Node:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent

    def nodes(self):
        return [self.left, self.right]


class Tree:
    def __init__(self, root=None):
        self.root = root

def find_node(node, to_delete):
    if node in to_delete:
        return None
    else:
        return node

def solution(tree, to_delete):
    roots = []
    subtree = [tree[0]]
    c = 0
    length = len(tree)
    level = 2

    for i in range(1, length):
        node = tree[i]

        if c == level:
            print(level, c)
            level *= 2
            c = 0
            subtree.append(find_node(node, to_delete))
            roots.append(subtree)
            subtree = []
        else:    
            subtree.append(find_node(node, to_delete))
        
        c += 1
        

    return roots



tree = [1, 2, 3, 4, 5, 6, 7]
to_delete = [3, 5]
result = solution(tree, to_delete)
print(result)