from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    res = 0
    while y:
        if y & 1:
            res = add(res, x)
        x <<= 1
        y >>= 1
    return res
    

def add(x: int, y: int) -> int:
    while y:
        carry = x & y
        x ^= y
        y = carry << 1
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
