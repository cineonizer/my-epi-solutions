from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    farthest_idx = 0
    for i in range(len(A)):
        if i > farthest_idx:
            return False
        farthest_idx = max(farthest_idx, A[i] + i)
    return True
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
