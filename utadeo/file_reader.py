#!/usr/bin/env python3

import os


def read_file(path):
    squares = []

    with open(path) as numbers_file, open('./data/squares.txt', 'w+') as squares_file:
        lines = numbers_file.readlines()
        
        for line in lines:
            n = '{}\n'.format(str(int(line) ** 2))
            squares_file.write(n)
            squares.append(n)

    return squares


def read_ops(path):
    squares = []

    with open(path) as ops_file, open('./data/ops_result.txt', 'w+') as results_file:
        lines = ops_file.readlines()
        
        for line in lines:
            s = line.replace('\n', '')
            op = eval(s)
            r = '{0} = {1}\n'.format(s, op)
            results_file.write(r)
    return squares


if __name__ == '__main__':
    content = read_ops('./data/ops.txt')

    print(content)
