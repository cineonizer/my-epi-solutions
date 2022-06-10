import functools
from re import S

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    # First, reverse the whole string.
    s.reverse()

    start = 0
    while start < len(s):
        next_whitespace = start
        while next_whitespace < len(s) and s[next_whitespace] != ' ':
            next_whitespace += 1
        reverse_range(s, start, next_whitespace - 1)
        start = next_whitespace + 1
    return s


    # solution similar to above but not O(1) space complexity because of s[start:next_whitespace] = reversed(s[start:next_whitespace])
    # s[start:next_whitespace] creates a new array everytime
    # slightly faster than the pythonic solution below
    s.reverse()
    
    start = 0
    while start < len(s):
        next_whitespace = start
        while next_whitespace < len(s) and not s[next_whitespace].isspace():
            next_whitespace += 1
        s[start:next_whitespace] = reversed(s[start:next_whitespace])
        start = next_whitespace + 1
    return s

    # my initial solution
    # used the next method below initially but made runtime slow since we are slicing at every indices of whitespaces: 
    # next_whitespace = next((i + start for i, c in enumerate(s[start:]) if c.isspace()), len(s))
    start = 0
    while start < len(s):
        next_whitespace = next((i for i in range(start, len(s)) if s[i].isspace()), len(s))
        s[start:next_whitespace] = reversed(s[start:next_whitespace])
        start = next_whitespace + 1
    s.reverse()
    return s

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
