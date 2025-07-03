"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/smallest-positive-missing-number-1587115621

You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.

Constraints:
1 <= arr.size() <= 105
-106 <= arr[i] <= 106
"""

from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        """
        Finds the smallest positive integer missing from the array.

        This uses index marking (in-place hashing):
        - Ignores negatives and zeros
        - Marks presence of numbers in [1, n] range by flipping the sign at their index
        - The first index with a positive number indicates the missing number

        Args:
            arr (List[int]): The input array.

        Returns:
            int: The smallest missing positive integer.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)

        # Step 1: Normalize the array — replace negatives and zeros with 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i] = 0

        # Step 2: Use indices to mark the presence of numbers
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                index = val - 1
                if arr[index] > 0:
                    arr[index] *= -1
                elif arr[index] == 0:
                    arr[index] = -(n + 1)  # Use a unique negative marker

        # Step 3: First index with a positive value is the missing number
        for i in range(n):
            if arr[i] >= 0:
                return i + 1

        # Step 4: If all numbers 1 to n are present
        return n + 1
