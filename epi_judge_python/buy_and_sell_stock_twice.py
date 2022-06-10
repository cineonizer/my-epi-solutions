from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    min_price_so_far, max_profit_so_far = float('inf'), 0
    total_profits = [0] * len(prices)
    for i, price in enumerate(prices):
        max_profit_so_far = max(max_profit_so_far, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)
        total_profits[i] = max_profit_so_far

    max_total_profit = 0

    max_price_so_far, max_profit_so_far = float('-inf'), 0
    for i, price in reversed(list(enumerate(prices))):
        max_profit_so_far = max(max_profit_so_far, max_price_so_far - price)
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, total_profits[i] + max_profit_so_far)

    return max_total_profit

    
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
