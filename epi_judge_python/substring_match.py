from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    # my solution using nested for loops O(n^2)
    if not s: return 0
    for i in range(len(t) - len(s) + 1):
        for j in range(len(s)):
            if t[i + j] != s[j]: break
            if j == len(s) - 1:
                return i
    return -1

    # my solution using slicing O(n^2)
    if not s: return 0
    for i in range(len(t)):
        if t[i] == s[0] and t[i:i + len(s)] == s:
            return i
    return -1

    # pythonic solution using find
    # return t.find(s)
        


        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
