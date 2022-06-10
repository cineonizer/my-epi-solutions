from test_framework import generic_test


def divide(x: int, y: int) -> int:
    pass

def subtract(x: int, y: int) -> int:
    while y:
        borrow = ~x & y
        x ^= y
        y = borrow << 1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
