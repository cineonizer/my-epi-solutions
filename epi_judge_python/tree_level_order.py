from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # book solution (20 ms)
    res = []
    if not tree: return res
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        res.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            neighbor for curr in curr_depth_nodes for neighbor in (curr.left, curr.right) if neighbor
        ]
    return res


    # similar to the book solution but actually use a queue data structure in the solution
    # res = []
    # if not tree: return []
    # q = collections.deque()
    # q.append([tree])
    # while q:
    #     curr_depth = q.popleft()
    #     res.append([curr_depth_node.data for curr_depth_node in curr_depth])
    #     neighbors = [neighbor for curr_depth_node in curr_depth for neighbor in (curr_depth_node.left, curr_depth_node.right) if neighbor]
    #     if neighbors: q.append(neighbors)
    # return res

    # my solution (first iteration) used a nested queue
    # if not tree: return []
    # res = []
    # q = collections.deque()

    # sub_q = collections.deque()
    # sub_q.append(tree)

    # q.append(sub_q)
    # while q:
    #     curr_depth = q.popleft()
    #     sub_res = []
    #     neighbors = collections.deque()
    #     while curr_depth:
    #         node_of_curr_depth = curr_depth.popleft()
    #         if node_of_curr_depth.left:
    #             neighbors.append(node_of_curr_depth.left)
    #         if node_of_curr_depth.right:
    #             neighbors.append(node_of_curr_depth.right)
    #         sub_res.append(node_of_curr_depth.data)
    #     if neighbors:
    #         q.append(neighbors)
    #     res.append(sub_res)
    # return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
