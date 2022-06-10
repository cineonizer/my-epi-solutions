import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    count_list_0, count_list_1 = get_length(l0), get_length(l1)
    
    longer_list = l0 if count_list_0 > count_list_1 else l1
    shorter_list = l1 if count_list_1 < count_list_0 else l0

    for _ in range(abs(count_list_0 - count_list_1)):
        longer_list = longer_list.next

    while longer_list and shorter_list:
        if longer_list is shorter_list:
            return longer_list
        longer_list, shorter_list = longer_list.next, shorter_list.next
    return None


def get_length(head: ListNode) -> int:
    count, curr = 0, head
    while curr:
        count, curr = count + 1, curr.next
    return count


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
