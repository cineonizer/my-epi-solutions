from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def traverse(tree, path_sum):
        if tree is None:
            return False

        path_sum += tree.data

        if tree.left is None and tree.right is None and path_sum == remaining_weight:
            return True

        return traverse(tree.left, path_sum) or traverse(tree.right, path_sum)
    return traverse(tree, 0)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
