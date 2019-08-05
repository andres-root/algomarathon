#!/usr/bin/env python3


def pat(pattern, string):
    pattern = list(pattern)
    string = string.split()

    if len(string) != len(pattern):
        return False

    ht = {}
    result = []

    for i in range(len(pattern)):
        if pattern[i] not in po.keys():
            ht[pattern[i]] = string[i]

        result.append(ht[pattern[i]])
    print(result)
    return (result == string)

if __name__ == '__main__':
    string = 'felipe luis luis felipe'
    pattern = 'abbab'

    result = pat(pattern, string)

    print(result)
