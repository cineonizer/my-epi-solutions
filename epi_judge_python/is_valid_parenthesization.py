from string import punctuation
from test_framework import generic_test
import collections

def is_well_formed(s: str) -> bool:
    punctuation = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    left_chars = []

    for c in s:
        if c in punctuation:
            left_chars.append(c)
        elif not left_chars or punctuation[left_chars.pop()] != c:
            return False
    return not left_chars # return True if stack is empty

    # my solution (ugly)
    left = {
        '{': 'brace',
        '(': 'parenthesis',
        '[': 'bracket'
    }
    right = {
        '}': 'brace',
        ')': 'parenthesis',
        ']': 'bracket'
    }
    
    stack = []
    for c in s:
        if c in left:
            stack.append(c)
        if c in right and (not stack or left[stack.pop()] != right[c]):
            return False
    return not stack
            


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
