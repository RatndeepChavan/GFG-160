"""
Link - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/next-permutation5226

Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order).

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is [3, 4, 5, 1, 2].

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
"""


class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Rearranges the array into the next lexicographically greater permutation.
        If such arrangement is not possible (i.e., the array is in descending order),
        it rearranges the array to the lowest possible order (sorted in ascending order).
        This modification is done in-place.

        Approach:
        1. Traverse from the end and find the first idex `pivot_index` where descending order breaks (arr[pivot_index] < arr[pivot_index + 1]).
        This is the point where the next permutation can be generated.
        2. If no such pivot exists, the array is the highest permutation — reverse the entire array.
        3. Otherwise, find the smallest element greater than arr[pivot_index] to the right of it, and swap them.
        4. Finally, reverse the subarray after index `pivot_index` to get the next smallest lexicographical order.

        Args:
            arr (List[int]): The input list of integers.

        Returns:
            None

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        def reverse_arr(start: int, end: int) -> None:
            """Reverses the subarray from index `start` to `end` in-place."""
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(arr)
        pivot_index = n - 2

        # Step 1: Find the pivot index where arr[pivot_index] < arr[pivot_index + 1]
        while pivot_index >= 0 and arr[pivot_index] >= arr[pivot_index + 1]:
            pivot_index -= 1

        # Step 2: If no pivot found, reverse the entire array
        if pivot_index == -1:
            reverse_arr(0, n - 1)
            return

        # Step 3: Find the next greater element on the right of pivot_index
        successor = n - 1
        while arr[pivot_index] >= arr[successor]:
            successor -= 1

        # Step 4: Swap pivot_index and successor, then reverse the tail
        arr[pivot_index], arr[successor] = arr[successor], arr[pivot_index]
        reverse_arr(pivot_index + 1, n - 1)
