from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    # rule: 0 - 255 inclusive
    # rule: no leading 0's
    # rule: 4 integers

    # a solution using backtracking since the textbook uses three nested loop and can be hard to read
    res = []
    if len(s) > 12: return res
    
    def backtrack(i, num_of_ints, ip_address):
        if num_of_ints == 4 and i > len(s) - 1:
            res.append(ip_address[:-1])
            return
        
        if num_of_ints > 4:
            return

        for j in range(i, min(i + 3, len(s))):
            if (s[i] != '0' or j == i) and 0 <= int(s[i:j + 1]) <= 255:
                backtrack(j + 1, num_of_ints + 1, ip_address + s[i:j + 1] + '.')

    backtrack(0, 0, '')
    return res

        

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
