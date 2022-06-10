from typing import List
import collections
import copy

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    for i in range(len(square_matrix) // 2):
        for j in range(i, len(square_matrix) - 1 - i):
            square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i] = square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i], square_matrix[i][j]

    # O(n^2) time and O(n) space complexity
    # H = collections.defaultdict(list)
    # n = len(square_matrix)

    # for idx, row in zip(reversed(range(n)), square_matrix):
    #     H[idx] = copy.copy(row)

    # for c in range(n):
    #     for r in range(n):
    #         square_matrix[r][c] = H.get(c)[r]


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
