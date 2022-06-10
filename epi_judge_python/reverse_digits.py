from test_framework import generic_test


def reverse(x: int) -> int:
    res = 0
    remaining_x = abs(x)
    while remaining_x:
        rem = remaining_x % 10
        res = (res * 10) + rem
        remaining_x //= 10
    return res if x > 0 else -res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
