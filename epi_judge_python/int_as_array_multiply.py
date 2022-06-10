from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0) != (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    res = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i + j + 1] += num1[i] * num2[j]
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10
    res = res[next((i for i, n in enumerate(res) if n != 0), len(res)):] or [0]
    res[0] *= sign
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
