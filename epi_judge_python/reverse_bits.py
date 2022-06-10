from test_framework import generic_test


def reverse_bits(x: int) -> int:
    for i, j in zip(range(32), reversed(range(32, 64))):
        if (x >> i) & 1 == (x >> j) & 1: continue
        x = (x ^ (1 << i)) ^ (1 << j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
