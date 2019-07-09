#!/usr/bin/env python3

import math


def karatsuba(a, b):
    """
    From: https://en.wikipedia.org/wiki/Karatsuba_algorithm

    procedure karatsuba(num1, num2)
        if (num1 < 10) or (num2 < 10)
            return num1*num2

        /* calculates the size of the numbers */
        m = min(size_base10(num1), size_base10(num2))
        m2 = floor(m/2) 
        /*m2 = ceil(m/2) will also work */

        /* split the digit sequences in the middle */
        high1, low1 = split_at(num1, m2)
        high2, low2 = split_at(num2, m2)

        /* 3 calls made to numbers approximately half the size */
        z0 = karatsuba(low1, low2)
        z1 = karatsuba((low1 + high1), (low2 + high2))
        z2 = karatsuba(high1, high2)

        return (z2 * 10 ^ (m2 * 2)) + ((z1 - z2 - z0) * 10 ^ m2) + z0
    """

    if a < 10 or b < 10:
        return a*b
    
    a = str(a)
    b = str(b)
    
    m = min(len(a), len(b))
    m2 = math.floor(m/2)

    a_high, a_low = int(a[:m2]), int(a[m2:])
    b_high, b_low = int(b[:m2]), int(b[m2:])

    print(a_high, a_low)

    z0 = karatsuba(a_low, b_low)
    z1 = karatsuba((a_low + a_high), (b_low + b_high))
    z2 = karatsuba(a_high, b_high)

    return (z2 * 10 ^ (m2 * 2)) + ((z1 - z2 - z0) * 10 ^ m2) + z0

if __name__ == '__main__':
    result = karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
    print(result)
    