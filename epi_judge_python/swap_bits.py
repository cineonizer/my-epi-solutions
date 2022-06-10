from test_framework import generic_test


def swap_bits(x, i, j):
    if not check_bits_differ(x, i, j): return x
    return x ^ (1 << i) ^ (1 << j)


def check_bits_differ(x, i, j):
    return (x >> i) & 1 != (x >> j) & 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
