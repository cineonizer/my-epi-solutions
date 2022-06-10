import functools
from re import sub
from typing import List

from regex import S

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    if not s: return 0
    slow = num_of_a = 0
    for fast in range(size):
        if s[fast] != 'b':
            s[slow] = s[fast]
            slow += 1
        if s[fast] == 'a':
            num_of_a += 1

    sublength = slow
    slow, fast = slow - 1, sublength + num_of_a - 1

    while fast > -1:
        if s[slow] == 'a':
            s[fast] = s[fast - 1] = 'd'
            fast -= 2
        else:
            s[fast] = s[slow]
            fast -= 1
        slow -= 1
    return sublength + num_of_a
    
    # my solution can be optimized by elimination sum and next methods
    # if not s: return 0
    # # overwrite all b's and shift the elements
    # slow = next((i for i, c in enumerate(s) if c == 'b'), len(s))
    # fast = slow + 1

    # while fast < len(s):
    #     if s[fast] != 'b':
    #         s[slow] = s[fast]
    #         slow += 1
    #     s[fast] = ''
    #     fast += 1

    # # replace all a's with two d's
    # num_of_a = s.count('a')
    # sublen = sum(1 for c in s if c)
    # new_len = num_of_a + sublen

    # slow = next((i for i, c in reversed(list(enumerate(s))) if c), 0)
    # fast = new_len - 1

    # while fast > -1:
    #     if s[slow] == 'a':
    #         s[fast] = s[fast - 1] = 'd'
    #         fast -= 2
    #     else:
    #         s[fast] = s[slow]
    #         fast -= 1
    #     slow -= 1
    # return new_len



@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
