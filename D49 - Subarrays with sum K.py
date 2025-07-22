"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/subarrays-with-sum-k

Given an unsorted array arr[] of integers, find the number of subarrays whose sum exactly equal to a given number k.

Examples:

Input: arr[] = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.
Input: arr[] = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.
Input: arr[] = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.

Constraints:
1 ≤ arr.size() ≤ 105
-103 ≤ arr[i] ≤ 103
-105 ≤ k ≤ 105
"""


class Solution:
    def cntSubarrays(self, arr, k):
        """
        Counts the number of subarrays whose sum equals k.

        ✅ Approach:
        - Use prefix sum and a hashmap to track the frequency of prefix sums.
        - For each element, compute the current prefix sum.
        - Check how many times (current_sum - k) has appeared before — those represent valid subarrays ending at the current index.
        - Update the prefix sum frequency map.

        ⏱️ Time: O(N), where N is the length of the array
        🧠 Space: O(N), for storing prefix sums in the hashmap
        """
        ans = current_sum = 0

        # Initialize with 0 sum to handle subarrays starting from index 0
        prefix_sum = {0: 1}

        for i in arr:
            current_sum += i
            required_sum = current_sum - k

            # If such a prefix exists, add its frequency to the answer
            if required_sum in prefix_sum:
                ans += prefix_sum[required_sum]

            # Update the frequency of the current prefix sum
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return ans
