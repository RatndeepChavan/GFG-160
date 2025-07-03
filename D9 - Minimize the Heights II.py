"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351

Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
Input: k = 3, arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11.

Constraints
1 ≤ k ≤ 107
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 107
"""

from typing import List


class Solution:
    def getMinDiff(self, arr: List[int], k: int) -> int:
        """
        Modifies the array by either increasing or decreasing each element by k exactly once,
        and returns the minimal possible difference between the maximum and minimum values
        of the modified array.

        Approach:
        - Sort the array.
        - The max difference without any operation is arr[n-1] - arr[0].
        - Iterate through the array and simulate increasing first `i` elements by `+k` and
        decreasing the rest by `-k`.
        - Track the minimal possible difference between modified max and min.

        Args:
            arr (List[int]): The list of integers representing tower heights.
            k (int): The value to be added or subtracted from each element.

        Returns:
            int: The minimized maximum difference after modification.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        n = len(arr)
        if n == 1:
            return 0  # Only one element, no difference

        arr.sort()

        # Initial difference without any modification
        min_diff = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] < k:
                continue  # Skipping as subtracting k would make it negative

            # Potential new min and max after modifying the elements
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[-1] - k, arr[i - 1] + k)

            # Update result if better
            min_diff = min(min_diff, max_height - min_height)

        return min_diff
