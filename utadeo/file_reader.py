#!/usr/bin/env python3


def read_file(path):
    with open(path) as f:
        lines = f.readlines()
    
    return lines


if __name__ == '__main__':
    content = read_file('./data/data.txt')

    print(content)
