from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

def decoding(s: str) -> str:
    res, num_of_char = [], 0
    for c in s:
        if c.isdigit():
            num_of_char = num_of_char * 10 + int(c)
        else:
            res.append(num_of_char * c)
            num_of_char = 0
    return ''.join(res)

    # my solution same idea, except the int(s[j:i]) will be slow since it has to slice everytime we come across a letter
    # res = []
    # j = 0
    # for i in range(1, len(s)):
    #     if s[i] in string.digits: continue
    #     res.append(int(s[j:i]) * s[i])
    #     j = i + 1
    # return ''.join(res)

def encoding(s: str) -> str:
    # my solution
    res = []
    j = 0
    for i in range(1, len(s)):
        if s[j] == s[i]: continue
        res.append(str(i - j) + s[j])
        j = i
    res.append(str(len(s) - j) + s[j])
    return ''.join(res)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
