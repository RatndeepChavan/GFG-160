"""
Link - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621

Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

Constraints:
1 <= arr.size(), d <= 105
0 <= arr[i] <= 105
"""

from typing import List


class Solution:
    def reverse_arr(self, start, end, arr):
        """
        Reverses a subarray in-place from index `start` to `end`.

        Args:
            start (int): Starting index of the subarray.
            end (int): Ending index of the subarray.
            arr (List[int]): The array being modified.
        """
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotateArr(self, arr: List[int], d: int) -> None:
        """
        Rotates the array to the left (counter-clockwise) by `d` elements in-place
        using the reversal algorithm.

        Approach:
        1. Reverse the first `d` elements.
        2. Reverse the remaining `n - d` elements.
        3. Reverse the entire array.
        NOTE : Reversing the order of approach will give same result.

        This results in a rotated array without using any extra space.

        Args:
            arr (List[int]): The input array to rotate.
            d (int): Number of positions to rotate the array.

        Returns:
            None

        Time Complexity: O(n), where n is the length of the array.
        Space Complexity: O(1), as the rotation is done in-place.
        """
        n = len(arr)

        # * Edge case where d > n
        # Rotating an array by its own length (or any multiple of it) results in the same array.
        # So we reduce d to its effective value using modulo.
        # For example, rotating a 5-element array by 7 is equivalent to rotating by 2 (7 % 5 = 2).
        d = d % n

        # If no rotation is needed (d is 0) or the array is empty, return early.

        if d == 0 or n == 0:
            return

        self.reverse_arr(0, d - 1, arr)  # Reverse first part
        self.reverse_arr(d, n - 1, arr)  # Reverse second part
        self.reverse_arr(0, n - 1, arr)  # Reverse the whole array
