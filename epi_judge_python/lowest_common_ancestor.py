import functools
from re import A
from turtle import right
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    SubtreeInfo = collections.namedtuple('SubtreeInfo', ('num_of_nodes', 'ancestor'))

    def traverse(tree: BinaryTreeNode):
        # textbook solution
        if not tree:
            return SubtreeInfo(0, None)

        left_subtree_info = traverse(tree.left)
        if left_subtree_info.num_of_nodes == 2:
            return left_subtree_info

        right_subtree_info = traverse(tree.right)
        if right_subtree_info.num_of_nodes == 2:
            return right_subtree_info

        num_of_nodes = left_subtree_info.num_of_nodes + right_subtree_info.num_of_nodes + (node0, node1).count(tree)
        ancestor = tree if num_of_nodes == 2 else None

        return SubtreeInfo(num_of_nodes, ancestor)
    return traverse(tree).ancestor

    """
    # first solution
    lca = None
    def traverse(tree: BinaryTreeNode):
        nonlocal lca

        if not tree or :
            return SubtreeInfo(0)

        left_subtree_info = traverse(tree.left)
        right_subtree_info = traverse(tree.right)

        num_nodes = left_subtree_info.nodes_present + right_subtree_info.nodes_present

        if tree == node0 or tree == node1:
            num_nodes += 1
        if tree == node0 == node1:
            num_nodes = 2
        if num_nodes == 2 and not lca:
            lca = tree

        return SubtreeInfo(num_nodes)

    traverse(tree)
    return tree if not lca else lca
    """
        

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
