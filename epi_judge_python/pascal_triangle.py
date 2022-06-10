from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    pascal_triangle = [[1] * i for i in range(1, n + 1)] # this list comprehension creates something like this when n = 5 -> [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
    for i in range(2, n):
        for j in range(1, i):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
    return pascal_triangle

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
