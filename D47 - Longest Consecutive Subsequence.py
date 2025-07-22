"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/longest-consecutive-subsequence2449


Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.
Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105
"""


class Solution:
    def longestConsecutive(self, arr):
        """
        Returns the length of the longest subsequence of consecutive integers.

        ✅ Approach:
        - Use a set for O(1) lookups
        - For each number, only start counting if it's the beginning of a sequence (i.e., no predecessor exists)
        - Expand the sequence as long as consecutive elements exist

        ⏱️ Time: O(N), where N is the number of elements in the array
        🧠 Space: O(N), due to the set used for lookups
        """

        tracker = set(arr)  # Set for fast lookups
        longest_sequence = 1  # Tracks maximum consecutive sequence length

        for num in arr:
            prev = num - 1

            # ! Skip if this is not the start of a sequence
            if prev in tracker:
                continue

            # * Start a new sequence
            nxt = num + 1
            cur_sequence = 1
            while nxt in tracker:
                nxt += 1
                cur_sequence += 1

            longest_sequence = max(longest_sequence, cur_sequence)

        return longest_sequence
