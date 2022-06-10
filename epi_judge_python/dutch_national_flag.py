import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    """
    # two pass (2 paritition solution)
    pivot = A[pivot_index]
    j = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[j] = A[j], A[i]
            j += 1
    j = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[j] = A[j], A[i]
            j -= 1    
    """
    # one pass (4 partition solution)
    pivot = A[pivot_index]
    i, mid_idx, top_idx = 0, 0, len(A)
    while i < top_idx:
        if A[i] < pivot:
            A[i], A[mid_idx] = A[mid_idx], A[i]
            mid_idx += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[top_idx - 1] = A[top_idx - 1], A[i]
            top_idx -= 1
        else:
            i += 1

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
    # dutch_flag_partition(0, [3, 1, 5, 2, 0, 1, 7, 3, 4])
