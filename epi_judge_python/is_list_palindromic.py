from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    first_half, second_half = L, reverse_list(slow)
    while second_half:
        if first_half.data != second_half.data: return False
        first_half, second_half = first_half.next, second_half.next
    return True

def reverse_list(head: ListNode) -> ListNode:
    prev_node, curr_node = None, head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
