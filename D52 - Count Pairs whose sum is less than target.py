"""
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-pairs-whose-sum-is-less-than-target

Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.

Examples:

Input: arr[] = [7, 2, 5, 3], target = 8
Output: 2
Explanation: There are 2 pairs with sum less than 8: (2, 5) and (2, 3).
Input: arr[] = [5, 2, 3, 2, 4, 1], target = 5
Output: 4
Explanation: There are 4 pairs whose sum is less than 5: (2, 2), (2, 1), (3, 1) and (2, 1).
Input: arr[] = [2, 1, 8, 3, 4, 7, 6, 5], target = 7
Output: 6
Explanation: There are 6 pairs whose sum is less than 7: (2, 1), (2, 3), (2, 4), (1, 3), (1, 4) and (1, 5).

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 104
1 <= target <= 104
"""


class Solution:
    def countPairs(self, arr, target):
        """
        Returns the count of pairs (i, j) such that i < j and arr[i] + arr[j] < target.

        ✅ Approach:
        - Sort the array to use two-pointer technique efficiently.
        - Initialize two pointers: `start` at beginning, `end` at end.
        - If current sum < target, then all pairs between start and end are valid.
        - Move pointers accordingly to explore remaining pairs.

        ⏱️ Time: O(N log N) due to sorting
        🧠 Space: O(1)
        """

        # * Required for two-pointer strategy
        arr.sort()

        pairs_count = 0
        start = 0
        end = len(arr) - 1

        while start < end:
            addition = arr[start] + arr[end]

            if addition >= target:
                # If sum is too large, try a smaller number
                end -= 1
            else:
                # All elements from start+1 to end will form valid pairs
                pairs_count += end - start
                start += 1

        return pairs_count
