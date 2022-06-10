from calendar import c
from cgitb import small
from turtle import right
from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    if len(perm) < 2: return []

    curr_idx = len(perm) - 1
    while curr_idx > 0:
        if perm[curr_idx - 1] < perm[curr_idx]:
            swap_el_with_the_smallest_el(curr_idx - 1, perm)
            reverse_subarray(curr_idx, len(perm) - 1, perm)
            return perm
        curr_idx -= 1
    return []

def swap_el_with_the_smallest_el(idx_of_el_to_be_swapped: int, perm: List[int]) -> None:
    curr_idx, smallest_el_idx = idx_of_el_to_be_swapped + 1, 0
    while curr_idx < len(perm) and perm[curr_idx] > perm[idx_of_el_to_be_swapped]:
        smallest_el_idx = curr_idx
        curr_idx += 1
    perm[idx_of_el_to_be_swapped], perm[smallest_el_idx] = perm[smallest_el_idx], perm[idx_of_el_to_be_swapped]

def reverse_subarray(start_idx: int, end_idx: int, perm: List[int]) -> None:
    while start_idx < end_idx:
        perm[start_idx], perm[end_idx] = perm[end_idx], perm[start_idx]
        start_idx, end_idx = start_idx + 1, end_idx - 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
