from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    kth_ahead = L
    for _ in range(k):
        kth_ahead = kth_ahead.next
    head = curr = ListNode(0, L)
    while kth_ahead:
        curr, kth_ahead = curr.next, kth_ahead.next
    curr.next = curr.next.next
    return head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
