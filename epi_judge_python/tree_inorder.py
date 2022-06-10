from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack, res = [], []
    while stack or tree:
        while tree:
            stack.append(tree)
            tree = tree.left
        tree = stack.pop()
        res.append(tree.data)
        tree = tree.right
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
