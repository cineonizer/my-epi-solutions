from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n, i = len(square_matrix), 0
    total_num_of_el = n * n
    res = []
    while len(res) != total_num_of_el:
        traverse_right(square_matrix, n, i, res)
        traverse_down(square_matrix, n, i, res)
        traverse_left(square_matrix, n, i, res)
        traverse_up(square_matrix, n, i, res)
        i += 1
    return res    

def traverse_right(square_matrix: List[List[int]], n: int, i: int, res: List[int]) -> None:
    """
    n: number of elements along the square edge
    i: index of the current spiral sequence, i.e. a spiral sequence consists of the pattern 'RDLU'
    """
    # r is the index of the current row
    r = i
    for c in range(0 + i, n - i, 1):
        res.append(square_matrix[r][c])

def traverse_down(square_matrix: List[List[int]], n: int, i: int, res: List[int]) -> None:
    # c is the index of the current col
    c = n - 1 - i
    for r in range(1 + i, n - i, 1):
        res.append(square_matrix[r][c])

def traverse_left(square_matrix: List[List[int]], n: int, i: int, res: List[int]) -> None:
    r = n - 1 - i
    for c in range(n - 2 - i, -1 + i, -1):
        res.append(square_matrix[r][c])

def traverse_up(square_matrix: List[List[int]], n: int, i: int, res: List[int]) -> None:
    c = i
    for r in range(n - 2 - i, 0 + i, -1):
        res.append(square_matrix[r][c])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
