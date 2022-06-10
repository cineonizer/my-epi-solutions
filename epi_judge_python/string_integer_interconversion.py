from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    str_arr = []
    while True:
        str_arr.append(string.digits[x % 10])
        x //= 10
        if not x: break
    if is_negative: str_arr.append('-')
    return ''.join(reversed(str_arr))


def string_to_int(s: str) -> int:
    res = 0
    for c in s:
        if c in '-+': continue
        res *= 10
        res += string.digits.index(c)
    return -res if s[0] == '-' else res



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
