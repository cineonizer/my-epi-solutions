from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # get length of linked list
    count, temp = 0, L
    while temp:
        count, temp = count + 1, temp.next
    # return immediately if there is no list or shift factor is a perfect cycle (no remainder)
    if L is None or k % count == 0: return L

    # reset shift factor k to a new k if k > length of linked list
    k = k % count
    head = tail = new_tail = L
    idx = 1
    while tail.next:
        if idx + k == count:
            new_tail = tail
        idx, tail = idx + 1, tail.next
    new_head = new_tail.next
    tail.next = head
    new_tail.next = None
    return new_head





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
