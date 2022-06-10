import functools
from turtle import end_fill
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from do_terminated_lists_overlap import overlapping_no_cycle_lists
from is_list_cyclic  import has_cycle

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    root0, root1 = has_cycle(l0), has_cycle(l1)
    # case when both lists do not have cycles then just implement 7.4 solution
    if not root0 and not root1:
        return overlapping_no_cycle_lists(l0, l1)
    # case when only one linked list has a cycle then intersection is not possible
    elif (not root0 and root1) or (root0 and not root0):
        return None
    # case when both linked lists have cycles

    # traverse from the starting node of the list0's cycle and check if it comes across any node of the root1, which means it overlaps
    # if the temp reaches back to the start (root0) then there was no overlap so break
    temp = root0
    while temp:
        temp = temp.next
        # if temp finds a node or comes back to the start then break
        if temp is root1 or temp is root0:
            break
    # return any of the node in the cycle else None
    return root0 if temp is root1 else None
    



@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
