"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/equilibrium-point-1587115620

Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists.

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.

Constraints:
3 <= arr.size() <= 105
-104 <= arr[i] <= 104
"""


class Solution:
    def findEquilibrium(self, arr):
        """
        ✅ Approach:
            - Calculate the total sum of the array.
            - Traverse the array while maintaining the sum of elements to the left.
            - At each index, subtract the current element from total to get the sum on the right.
            - If left sum == right sum ⇒ equilibrium point.

        ⏱️ Time Complexity: O(n)
            - One pass to calculate total sum, one pass to find the equilibrium point.

        🧠 Space Complexity: O(1)
            - No extra data structures used, just scalar variables.

        ! If no equilibrium index is found, return -1.

        ? Left and right sums are compared **excluding** the current element.

        Args:
            arr (List[int]): List of integers.

        Returns:
            int: Index of the equilibrium point if found, else -1.
        """
        total_sum = sum(arr)  # Total sum of the array
        left_sum = 0  # Running sum of elements to the left

        for i in range(len(arr)):
            current = arr[i]
            total_sum -= current  # Now total_sum represents right sum

            # * ✅ Found equilibrium point
            if left_sum == total_sum:
                return i

            # Update left sum for next index
            left_sum += current

        # ! No equilibrium point found
        return -1
