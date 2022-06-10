import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = 0
        while node:
            depth, node = depth + 1, node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))

    short, long = node0, node1
    if depth0 > depth1:
        short, long = long, short
    
    for _ in range(abs(depth0 - depth1)):
        long = long.parent

    while long is not short:
        short, long = short.parent, long.parent
    return short

    """
    # O(h) and O(h) time and space complexity
    # since we have to store the nodes 
    node0_ancestors, node1_ancestors = [], []

    node0_ancestor = node0
    while node0_ancestor:
        node0_ancestors.append(node0_ancestor)
        node0_ancestor = node0_ancestor.parent
    
    node1_ancestor = node1
    while node1_ancestor:
        node1_ancestors.append(node1_ancestor)
        node1_ancestor = node1_ancestor.parent

    shorter, longer = node0_ancestors, node1_ancestors
    if len(shorter) > len(longer):
        shorter, longer = node1_ancestors, node0_ancestors

    for i, e in enumerate(shorter):
        if shorter[i] == longer[i + len(longer) - len(shorter)]:
            return e
    return shorter[-1]
    """

    


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
