import functools
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_subset(n: int, k: int) -> List[int]:

    # brute force method time complexity: O(n) to create array, O(k) to create random subset
    # space complexity: O(n) to create the array

    # superset = [i for i in range(n)]
    # for i in range(k):
    #     random_idx = random.randint(i, n - 1)
    #     superset[i], superset[random_idx] = superset[random_idx], superset[i]
    # return superset[:k]

    # faster method: O(k) space and time complexity use a hash map
    subset = {}
    for i in range(k):
        random_idx = random.randrange(i, n)
        random_idx_mapped = subset.get(random_idx, random_idx)
        i_mapped = subset.get(i, i)
        subset[random_idx] = i_mapped
        subset[i] = random_idx_mapped
    return [subset[i] for i in range(k)]

@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
