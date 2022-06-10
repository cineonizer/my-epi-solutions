from typing import Iterator, List

from regex import R

from test_framework import generic_test
import collections

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # iterator version (building heights are given one by one)
    Building = collections.namedtuple('Building', ('index', 'height'))
    
    stack, max_height = [], 0
    for index, height in enumerate(sequence):
        while stack and height >= stack[-1].height:
            stack.pop()
        stack.append(Building(index, height))
    return [building.index for building in reversed(stack)]

    # non-iterator version (building heights are given all together)
    if not sequence: return []
    max_height, stack = sequence[-1], [len(sequence) - 1] + []
    for index, height in reversed(list(enumerate(sequence))):
        if height > max_height:
            max_height = height
            stack.append(index)
    return stack

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
