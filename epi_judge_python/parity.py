from test_framework import generic_test


def parity(x: int) -> int:
    num_of_ones = 0
    while x:
        x &= (x - 1)
        num_of_ones += 1
    return 1 if num_of_ones % 2 else 0



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
