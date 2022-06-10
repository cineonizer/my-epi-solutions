from turtle import right
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def traverse(tree: BinaryTreeNode, path):
        if not tree:
            return 0
        
        path = path << 1 | tree.data

        if not tree.left and not tree.right:
            return path

        return traverse(tree.left, path) + traverse(tree.right, path)
    return traverse(tree, 0)

    """
    # my first solution
    def traverse(tree: BinaryTreeNode, path):
        if not tree:
            return 0

        left_path = traverse(tree.left, (path << 1) | tree.data)
        right_path = traverse(tree.right, (path << 1) | tree.data)

        if not left_path and not right_path:
            return (path << 1) | tree.data 
        
        sum_so_far = left_path + right_path

        return sum_so_far
    return traverse(tree, 0)
    """
        
        



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
