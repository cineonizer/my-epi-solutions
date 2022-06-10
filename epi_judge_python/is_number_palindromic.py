from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    res = 0
    remaining_x = abs(x)
    while remaining_x:
        rem = remaining_x % 10
        res = (res * 10) + rem
        remaining_x //= 10
    return res == x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
