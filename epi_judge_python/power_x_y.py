from test_framework import generic_test


def power(x: float, y: int) -> float:
    res = 1
    # accounting for negative powers
    if y < 0:
        x = 1 / x
        y = -y
    # iterate and halve the power so that we are performing binary exponentiation
    while y:
        if y & 1:
            res *= x
        x *= x
        y >>= 1 # halving the number
    return res

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
