"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/longest-sub-array-with-sum-k0809

Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.
Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

Constraints:
1 ≤ arr.size() ≤ 105
-104 ≤ arr[i] ≤ 104
-109 ≤ k ≤ 109
"""


class Solution:
    def longestSubarray(self, arr, k):
        """
        ✅ Approach:
            - Use prefix sum to track running totals.
            - Use a hashmap (sum_tracker) to store the **first occurrence** of each prefix sum.
            - At each index, compute (prefix_sum - k). If it exists in the map,
              that means there is a subarray summing to `k`.

        ⏱️ Time Complexity: O(n)
            - Single pass through the array with constant-time lookups.

        🧠 Space Complexity: O(n)
            - Hashmap to store prefix sums.

        ! Important:
            - Store first occurrence of each prefix sum only.
              This ensures longest subarray (earliest start index).
            - Don't overwrite if prefix_sum already exists in the map.

        Args:
            arr (List[int]): Array of integers (can be negative).
            k (int): Target sum.

        Returns:
            int: Length of the longest subarray with sum == k.
        """
        sum_tracker = {}  # ? Maps prefix_sum → earliest index
        max_len = 0
        prefix_sum = 0

        for idx in range(len(arr)):
            prefix_sum += arr[idx]
            required_sum = prefix_sum - k

            # * Case when subarray starts from index 0
            if prefix_sum == k:
                max_len = idx + 1

            # * Check if there's a previous prefix_sum equal to required_sum
            elif required_sum in sum_tracker:
                prev_idx = sum_tracker[required_sum]
                subarray_len = idx - prev_idx
                max_len = max(max_len, subarray_len)

            # ! Store only first occurrence of each prefix_sum
            if prefix_sum not in sum_tracker:
                sum_tracker[prefix_sum] = idx

        return max_len
