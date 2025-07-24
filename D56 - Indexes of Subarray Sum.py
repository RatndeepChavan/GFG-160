"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/subarray-with-given-sum-1587115621

Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.

Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 103
0 <= target <= 109
"""


class Solution:
    def subarraySum(self, arr, target):
        """
        Finds a continuous subarray that sums to the target.
        (1-based indexing for return)

        ✅ Approach:
        - Use sliding window technique.
        - Expand the window by moving `right`.
        - Shrink the window from `left` if the sum exceeds the target.
        - Return the 1-based index range if a matching sum is found.

        ⏱️ Time: O(N), where N is the length of the array (Worst case : O(N^2)
        🧠 Space: O(1), only variables used
        """

        left = 0
        right = 0
        current_sum = 0

        while right < len(arr):
            current_sum += arr[right]  # Expand the window to the right

            # * Check if current window matches the target
            if current_sum == target:
                return [left + 1, right + 1]  # NOTE: 1-based indexing

            # ! If sum exceeds target, shrink window from the left
            elif current_sum > target:
                while current_sum > target and left <= right:
                    current_sum -= arr[left]
                    left += 1

                # Recheck after shrinking
                if current_sum == target:
                    return [left + 1, right + 1]

            # Move right forward to expand window
            right += 1

        return [-1]  # ! No valid subarray found
