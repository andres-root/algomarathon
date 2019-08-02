#!/usr/bin/env python3


def reverse(s):
    if len(s) == 0:
        return ''
    else:
        return '{0}{1}'.format(reverse(s[1:]), s[0])

def test(test_cases):
    results = []

    for n in test_cases:
        results.append(
            '{0}lol'.format(reverse(n))
        )
    
    return results


if __name__ == '__main__':
    test_cases = ['arepa', 'utadeo']
    print(list(zip(test_cases, test(test_cases))))
