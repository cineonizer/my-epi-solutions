from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # my solution based on my pseudocode
    head = slow = L
    while slow and slow.next:
        if slow.data == slow.next.data:
            fast = slow.next.next
            while fast and fast.data == slow.data:
                fast = fast.next
            slow.next = fast
        else:
            slow = slow.next
    return head

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
