from tabnanny import check
from turtle import left, right
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced_status', 'height'))
    def check_balance(tree: BinaryTreeNode) -> BalancedStatusWithHeight:
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balance(tree.left)

        if not left_result.balanced_status:
            return left_result

        right_result = check_balance(tree.right)

        if not right_result.balanced_status:
            return right_result

        # this is slower than having two if statements because it won't traverse
        # if not left_result.balanced_status or not right_result.balanced_status:
        #     return BalancedStatusWithHeight(False, None)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balance(tree).balanced_status


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
