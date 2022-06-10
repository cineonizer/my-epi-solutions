from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # assign the short and long variables
    long, short = L1, L2
    # if the length of L1 is actually shorter then swap the two assignments
    if get_length(L1) < get_length(L2):
        long, short = short, long
    
    long_head = long
    while short or long:
        sum_of_nodes = (short.data if short else 0) + long.data
        if long.next:
            long.next.data += sum_of_nodes // 10
        # if long.next is None then that means we have reached the end of the longer list
        # so check if the last node's data is two digits if it is then create a new node for the first digit
        else:
            if sum_of_nodes > 9:
                long.next = ListNode(sum_of_nodes // 10, None)
        long.data = sum_of_nodes % 10
        short = short.next if short else None
        long = long.next
    return long_head
    
def get_length(L):
    count = 0
    while L:
        count, L = count + 1, L.next
    return count

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
