"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-pairs-with-given-sum--150253

Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] which sums up to given target.

Examples:

Input: arr[] = [1, 5, 7, -1, 5], target = 6
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5).
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).
Input: arr[] = [10, 12, 10, 15, -1], target = 125
Output: 0

Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
1 <= target <= 104
"""


class Solution:
    def countPairs(self, arr, target):
        """
        Counts the number of unique pairs in the array whose sum equals the given target.

        ✅ Approach:
        - Use a hash map to track the frequency of elements seen so far.
        - For each current element, compute its required complement (target - current).
        - If the complement exists in the map, it contributes as many pairs as its frequency.
        - Update the frequency of the current element in the map.

        ⏱️ Time: O(N), where N is the length of the array
        🧠 Space: O(N), for the hash map used to track frequencies
        """

        value_tracker = {}  # Stores frequencies of elements seen so far
        pairs_found = 0  # Counts valid pairs found

        for current_value in arr:
            required_value = target - current_value

            # If require value found, increase the valid pairs times require value frequency
            pairs_found += value_tracker.get(required_value, 0)

            # Increment frequency of the current value by 1
            value_tracker[current_value] = value_tracker.get(current_value, 0) + 1

        return pairs_found  # return total pairs found
