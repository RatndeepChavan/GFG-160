"""
Link :https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604

Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.
Input: arr[] = [2, 3, 4]
Output: 24
Explanation: For an array with all positive elements, the result is product of all elements.

Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10
"""

from typing import List


class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        """
        Finds the maximum product of any contiguous subarray.

        Approach:
        - Traverse the array twice:
            - Left-to-right: handles positive product chains
            - Right-to-left: handles negative product chains that turn positive when reversed
        - Reset the running product when a zero is encountered.

        Args:
            arr (List[int]): List of integers.

        Returns:
            int: Maximum product of any contiguous subarray.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)

        if n == 1:
            return arr[0]  # Only one element

        max_product = float("-inf")
        current_product = 1

        # Left-to-right pass
        for num in arr:
            current_product *= num
            max_product = max(max_product, current_product)

            if current_product == 0:
                current_product = 1  # Reset on zero

        # Right-to-left pass
        current_product = 1
        for i in reversed(range(n)):
            current_product *= arr[i]
            max_product = max(max_product, current_product)

            if current_product == 0:
                current_product = 1  # Reset on zero

        return max_product
