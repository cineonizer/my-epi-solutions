from test_framework import generic_test
import string
import functools

def ss_decode_col_id(col: str) -> int:
    # pythonic solution using reduce 
    alpha_map = {char: val for char, val in zip(string.ascii_uppercase, range(1, 27))}
    return functools.reduce(lambda acc, tup: acc + 26 ** tup[0] * alpha_map[tup[1]], enumerate(reversed(col)), 0) 

    # iteratively 
    # encoded_int = 0
    # for idx, char in enumerate(reversed(col)):
    #     encoded_int += 26 ** idx * alpha_map[char]
    # return encoded_int
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
