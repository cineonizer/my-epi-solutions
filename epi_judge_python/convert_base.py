from test_framework import generic_test

import functools
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    
    is_negative = num_as_string[0] == '-'

    # convert the given input string in base b1 into base 10 (decimal) using a reduce method and a lambda function
    #   acc: accumulation
    #   tup: current tuple of enumerate(reversed(num_as_string)) with (tup[0], tup[1]) as (idx, el)
    #   e.g. num_as_string as "615" with b1 as 7 will result in (((0 + "5" * (7 ** 0)) + "1" * (7 ** 1)) + "6" * (7 ** 2)) = 306

    #   string.hexdigits = 0123456789abcdefABCDEF
    #   so string.hexdigits.index(tup[1].lower()) is converting an input string with any letters "'A' as 10, 'B' as 11, 'C' as 12,..., 'F' as 15" 

    #   num_as_string[is_negative:] is python slicing with a boolean since boolean is of an int type with True as 1 and False as 0
    #   so if a string has '-' sign then num_as_string is sliced from index 1 (True) else num_as_string is sliced from index 0 (False)
    num_as_int = functools.reduce(lambda acc, tup: acc + int(string.hexdigits.index(tup[1].lower())) * (b1 ** tup[0]), enumerate(reversed(num_as_string[is_negative:])), 0)
    res = []
    while num_as_int:  
        res.append(string.hexdigits[num_as_int % b2].upper())
        num_as_int //= b2
    return ('-' if is_negative else '') + ('0' if not res else ''.join(reversed(res)))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
