#!/usr/bin/env python3


def pat(pattern, words):
    pattern = list(pattern)
    string = words.split()

    if len(string) != len(pattern) or words.strip()  == '':
        return False

    ht = {}
    result = []

    for i in range(len(pattern)):
        if pattern[i] not in ht.keys():
            ht[pattern[i]] = string[i]

        result.append(ht[pattern[i]])
    print(ht, result)
    return (result == string)


if __name__ == '__main__':
    string = 'felipe felipe luis luis felipe'
    pattern = 'abbac'

    result = pat(pattern, string)

    print(result)
