"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/largest-subarray-of-0s-and-1s

Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1
"""

# 0 0 1 0 1 1 1 0 0 0 1 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0


class Solution:
    def maxLen(self, arr):
        """
        ✅ Approach:
            - Convert all 0s in the array to -1.
              This transforms the problem into finding the longest subarray with sum = 0.
            - Use prefix sum + hashmap:
              Store the first occurrence of each prefix sum to compute subarray lengths.

        ⏱️ Time Complexity: O(n)
            - Single traversal with constant-time hashmap operations.

        🧠 Space Complexity: O(n)
            - Hashmap to store prefix sums and their first occurrence index.

        ! If prefix_sum becomes 0, subarray from index 0 to i has equal 0s and 1s.

        ? Why prefix_sum == 0 is special:
            - It means total number of 1s and -1s seen so far are equal.

        Args:
            arr (List[int]): Binary array containing only 0s and 1s.

        Returns:
            int: Length of the longest subarray with equal number of 0s and 1s.
        """
        sum_tracker = {}  # prefix_sum -> first index
        prefix_sum = 0
        max_len = 0

        for i in range(len(arr)):
            # * Convert 0 to -1 to enable sum-based logic
            value = 1 if arr[i] == 1 else -1
            prefix_sum += value

            # ? Entire subarray from 0 to i is balanced
            if prefix_sum == 0:
                max_len = i + 1

            elif prefix_sum in sum_tracker:
                prev_i = sum_tracker[prefix_sum]
                sub_len = i - prev_i
                max_len = max(max_len, sub_len)

            # ? Only store first occurrence to ensure longest subarray
            if prefix_sum not in sum_tracker:
                sum_tracker[prefix_sum] = i

        return max_len
