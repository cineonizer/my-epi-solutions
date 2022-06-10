from typing import List
import collections
from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    grids = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if partial_assignment[r][c] == 0: continue
            if partial_assignment[r][c] in rows[r] or partial_assignment[r][c] in cols[c] or partial_assignment[r][c] in grids[(r // 3, c // 3)]:
                return False
            rows[r].add(partial_assignment[r][c])
            cols[c].add(partial_assignment[r][c])
            grids[(r // 3, c // 3)].add(partial_assignment[r][c])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
