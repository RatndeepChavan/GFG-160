"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2

Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
Input: prices[] = [7, 6, 4, 3, 1]
Output: 0
Explanation: Here the prices are in decreasing order, hence if we buy any day then we cannot sell it at a greater price. Hence, the answer is 0.
Input: prices[] = [1, 3, 6, 9, 11]
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1].

Constraint:
1 <= prices.size()<= 105
0 <= prices[i] <=104
"""

from typing import List


class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit achievable from a single buy and sell transaction.

        The goal is to buy at the lowest price before a higher selling price.
        You can only make at most one transaction.

        Approach:
        - Track the minimum price seen so far (best day to buy).
        - At each step, calculate profit if we sold today.
        - Update the max profit accordingly.

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum profit from one transaction, or 0 if no profit possible.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update to new lowest price (buying point)
            else:
                max_profit = max(max_profit, price - min_price)  # Profit if sold today

        return max_profit
