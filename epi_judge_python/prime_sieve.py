from typing import List
from xmlrpc.client import Boolean

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    if n < 2: return []
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, n // 2 + 1):
        if is_prime[i]:
            for j in range(i * 2, len(is_prime), i):
                is_prime[j] = False
    return [i for i, b in enumerate(is_prime) if b]
    
    # O(n^1.5) solution
    # res = []
    # for i in range(2, n + 1):
    #     if is_prime(i): res.append(i)
    # return res

# def is_prime(n: int) -> bool:
#     for i in range(2, int(n ** (1 / 2) + 1)):
#         if n % i == 0: return False
#     return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
