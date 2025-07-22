"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/find-all-triplets-with-zero-sum

Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero.
Returned triplet should also be internally sorted i.e. i<j<k.

Examples:

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: Triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0
Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0
Input: arr[] = [2, 3, 1, 0, 5]
Output: [[]]
Explanation: There is no triplet with sum 0.

Constraints:
3 <= arr.size() <= 103
-104 <= arr[i] <= 104
"""


class Solution:
    def findTriplets(self, arr):
        """
        Finds all unique triplets (i, j, k) such that:
        arr[i] + arr[j] + arr[k] == 0 and i, j, k are distinct indices.

        ✅ Approach:
        - First, store all pairwise sums in a hash map: sum -> list of index pairs
        - Then for each element `arr[k]`, check if `-arr[k]` exists in the map
        - If so, loop through matching index pairs (i, j) to find valid triplets
        - Use a set to store sorted triplet indices to avoid duplicates

        ⏱️ Time: O(N²), due to double loops for pair sum and checking triplets
        🧠 Space: O(N²), for storing pair sums in a dictionary
        """

        idx_tracker = {}  # * Maps sum of pairs to list of index pairs
        ans = set()  # * Stores unique triplets as sorted tuples of indices

        # * Build map of all possible pairwise sums
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                total = arr[i] + arr[j]
                if total not in idx_tracker:
                    idx_tracker[total] = [[i, j]]
                else:
                    idx_tracker[total].append([i, j])

        # * For each index k, check if any pair sums to -arr[k]
        for k in range(len(arr)):
            target = -arr[k]
            if target in idx_tracker:
                for i, j in idx_tracker[target]:
                    # ! Ensure indices i, j, k are distinct
                    if i != k and j != k and i != j:
                        triplet = tuple(sorted([i, j, k]))
                        ans.add(triplet)

        return ans
