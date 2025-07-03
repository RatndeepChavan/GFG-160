"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620

Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.
Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

Constraints:
1 ≤ arr.size() ≤ 105
-109 ≤ arr[i] ≤ 104
"""

from typing import List


class Solution:
    def maxSubArraySum(self, arr: List[int]) -> int:
        """
        Finds the maximum sum of any contiguous subarray using Kadane's Algorithm.

        Approach:
        - Initialize two variables:
            - `current_sum` to store the ongoing subarray sum
            - `maximum_sum` to keep track of the highest subarray sum seen so far
        - Iterate through the array, updating both values.
        - If the current sum becomes negative, reset it to 0 (start a new subarray).

        Args:
            arr (List[int]): List of integers.

        Returns:
            int: Maximum sum of any contiguous subarray.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current_sum = 0
        maximum_sum = float("-inf")  # Handles arrays with all negative numbers

        for num in arr:
            current_sum += num
            maximum_sum = max(maximum_sum, current_sum)

            # If current_sum drops below 0, discard and start a new subarray
            if current_sum < 0:
                current_sum = 0

        return maximum_sum
