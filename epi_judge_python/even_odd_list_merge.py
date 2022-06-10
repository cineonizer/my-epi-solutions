from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # get the length of the linked list
    count, temp = 0, L
    while temp:
        count, temp = count + 1, temp.next
    # if the length of the linked list is smaller than 3 (either 1 or 2) then it's already merged (even) or (even, odd)
    if count < 3: return L

    even_head, odd_head = L, L.next
    even, odd = even_head, odd_head

    while even.next and odd.next:
        even.next, odd.next = even.next.next, odd.next.next
        even, odd = even.next, odd.next
    even.next = odd_head
    return even_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
