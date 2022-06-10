import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    # O(n)
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # finds the length of the cycle and offsets where the pointer starts by the cycle length
            offset_iter = head
            for _ in range(get_cycle_len(slow)):
                offset_iter = offset_iter.next
            # finds the start of the cycle by advancing both pointers in tandem
            non_offset_iter = head
            while offset_iter is not non_offset_iter:
                offset_iter, non_offset_iter = offset_iter.next, non_offset_iter.next  
            return non_offset_iter
    return None

def get_cycle_len(start) -> int:
    count, end = 0, start
    while True:
        count += 1
        start = start.next
        if start is end:
            return count

    # brute force solution O(n^2)
    # the outer loop traverses the nodes one-by-one
    # the inner loop starts from the head and traverses as many nodes as the outer loops gone through so far
    # if the node being visited by the outer loop is visited twice, then the cycle starts at that node
    
    # slow_pointer, slow_count = head, 1
    # while slow_pointer:
    #     fast_pointer = head
    #     slow_pointer_seen = 0
    #     for _ in range(slow_count):
    #         if fast_pointer is slow_pointer:
    #             slow_pointer_seen += 1
    #         if slow_pointer_seen == 2:
    #             return slow_pointer
    #         fast_pointer = fast_pointer.next
    #     slow_pointer, slow_count = slow_pointer.next, slow_count + 1
    # return None
            


        


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
