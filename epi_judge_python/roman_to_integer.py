from calendar import c
from test_framework import generic_test

import functools


def roman_to_integer(s: str) -> int:
    D = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return functools.reduce(lambda acc, i: acc + (-D[s[i]] if D[s[i + 1]] > D[s[i]] else D[s[i]]), reversed(range(len(s) - 1)), D[s[-1]])

    # non-pythonic solution
    i, res = len(s) - 2, D[s[len(s) - 1]]
    while i >= 0:
        val = -D[s[i]] if D[s[i + 1]] > D[s[i]] else D[s[i]]
        res += val
        i -= 1
    return res




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
