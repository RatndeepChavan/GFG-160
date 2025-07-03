"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615

The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

Examples:

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 - 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 - 40 = 655. Maximum Profit = 210 + 655 = 865.


Input: prices[] = [4, 2, 2, 2, 4]
Output: 2
Explanation: Buy the stock on day 3 and sell it on day 4 => 4 - 2 = 2. Maximum Profit = 2.

Constraints:
1 <= prices.size() <= 105
0 <= prices[i] <= 104
"""

from typing import List


class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from an array of stock prices,
        where multiple buy-sell transactions are allowed.
        You can buy and sell multiple times,
        but cannot hold more than one stock at a time.

        Greedy Approach:
        - Find a local minimum (buy point).
        - Wait until the local maximum (sell point).
        - Add the profit and reset for the next potential transaction.

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum profit possible.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        profit = 0
        buy_price = float("inf")  # Initialize with infinity to find the lowest price

        for i in range(len(prices)):
            # Update buy price to the lowest so far
            buy_price = min(buy_price, prices[i])

            # Check if current day is a local peak (i.e., price drops next day or it's the last day)
            is_last_day = i == len(prices) - 1
            is_peak = not is_last_day and prices[i + 1] < prices[i]

            if is_peak or is_last_day:
                profit += prices[i] - buy_price  # Sell at current price
                buy_price = float("inf")  # Reset to look for next buy opportunity

        return profit


# ! Clean & Short Greedy Approach


class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        """
        Greedy solution that adds up all profitable price differences
        between consecutive days where selling is beneficial.

        Idea:
        - Buy and sell on every rise in price.
        - This works because buying at valley and selling at peak
        gives the same profit as summing all incremental gains in between.

        Example:
        prices = [1, 5, 3, 8]
        Profit: (5 - 1) + (8 - 3) = 9
        Same as: (5 - 1) + (3 - 3) + (8 - 3) = 9

        Args:
            prices (List[int]): List of daily stock prices.

        Returns:
            int: Maximum profit possible.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
