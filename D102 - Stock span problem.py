"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/stock-span-problem-1587115621

The stock span problem is a financial problem where we have a series of daily price quotes for a stock and we need to calculate the span of stock price for all days.
You are given an array arr[] representing daily stock prices, the stock span for the i-th day is the number of consecutive days up to day i (including day i itself) for which the price of the stock is less than or equal to the price on day i. Return the span of stock prices for each day in the given sequence.

Examples:
Input: arr[] = [100, 80, 90, 120]
Output: [1, 1, 2, 4]
Explanation: Traversing the given input span 100 is greater than equal to 100 and there are no more days behind it so the span is 1, 80 is greater than equal to 80 and smaller than 100 so the span is 1, 90 is greater than equal to 90 and 80 so the span is 2, 120 is greater than 90, 80 and 100 so the span is 4. So the output will be [1, 1, 2, 4].
Input: arr[] = [10, 4, 5, 90, 120, 80]
Output: [1, 1, 2, 4, 5, 1]
Explanation: Traversing the given input span 10 is greater than equal to 10 and there are no more days behind it so the span is 1, 4 is greater than equal to 4 and smaller than 10 so the span is 1, 5 is greater than equal to 4 and 5 and smaller than 10 so the span is 2, and so on. Hence the output will be [1, 1, 2, 4, 5, 1].

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
"""

# ------------------------------------------------------------------
# * 🟢 1. Monotonic Stack (Optimal)
# ------------------------------------------------------------------
class SolutionStack:
    """
    🧩 Approach:
    ------------
    - Use a *monotonic decreasing stack* to keep track of previous higher prices.
    - Each element in the stack stores the index of a day whose price is **greater** than or equal to the current price.
    - When we find a price higher than or equal to the stack top, we pop it.
    - The distance between the current index and the previous greater price index gives the *span*.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N)**   (each index pushed/popped once)
    - 🧠 **Space: O(N)**  (stack to store indices)

    ✅ Most efficient and widely used method.
    """

    def calculateSpan(self, arr):
        n = len(arr)
        res = [1] * n
        stack = [0]  # stack holds indices

        for i in range(1, n):
            # Pop smaller or equal prices from stack
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # ? Why store index difference:
            # Because the span = current_index - previous_greater_index
            prev_greater = stack[-1] if stack else -1
            res[i] = i - prev_greater

            # Push current index for future comparisons
            stack.append(i)

        return res


# ------------------------------------------------------------------
# * 🟡 2. Brute Force (Naive)
# ------------------------------------------------------------------
class SolutionBrute:
    """
    🧩 Approach:
    ------------
    - For each day, look backward until you find a price greater than current.
    - Count how many consecutive days (including current) had lower or equal prices.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N²)**  (nested loops)
    - 🧠 **Space: O(1)**

    ❌ Inefficient for large N, but easy to understand conceptually.
    """

    def calculateSpan(self, arr):
        n = len(arr)
        res = [0] * n

        for i in range(n):
            span = 1
            j = i - 1
            while j >= 0 and arr[j] <= arr[i]:
                span += 1
                j -= 1
            res[i] = span
        return res


# ------------------------------------------------------------------
# * 🔴 3. Stack of (Value, Span) Pairs
# ------------------------------------------------------------------
class SolutionPairStack:
    """
    🧩 Approach:
    ------------
    - Maintain a stack storing tuples of (price, span).
    - For each new price:
        * While stack top ≤ current price, pop & accumulate spans.
        * Push (current_price, accumulated_span + 1).

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N)**
    - 🧠 **Space: O(N)**

    ✅ Alternative elegant variant using pairs instead of indices.
    """

    def calculateSpan(self, arr):
        stack = []  # stores (price, span)
        res = []

        for price in arr:
            span = 1
            while stack and stack[-1][0] <= price:
                prev_price, prev_span = stack.pop()
                span += prev_span

            stack.append((price, span))
            res.append(span)

        return res
