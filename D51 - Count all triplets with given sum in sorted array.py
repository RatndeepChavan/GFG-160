"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-all-triplets-with-given-sum-in-sorted-array

Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Four triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1.

Constraints:
3 ≤ arr.size() ≤ 104
-105 ≤ arr[i], target ≤ 105
"""


class Solution:
    def countTriplets(self, arr, target):
        """
        Counts the number of unique triplets in the array whose sum equals the target.

        ✅ Approach:
        - For every fixed element `arr[i]`, use two-pointer technique on the remaining subarray.
        - If sum of current triplet is less than target, move left pointer (ptr1) to increase sum.
        - If sum is greater than target, move right pointer (ptr2) to decrease sum.
        - If sum equals target, count the triplet and move ptr2 (and optionally temp for duplicates).

        ⏱️ Time: O(N^2)
        🧠 Space: O(1) — ignoring output count
        """

        arr.sort()  # * Sorting is important to use the two-pointer technique
        n = len(arr)
        triplets_found = 0

        for i in range(n):
            ptr1 = i + 1
            ptr2 = n - 1

            while ptr1 < ptr2:
                addition = arr[i] + arr[ptr1] + arr[ptr2]

                if addition > target:
                    ptr2 -= 1  # * Try smaller sum
                elif addition < target:
                    ptr1 += 1  # * Try larger sum
                else:
                    # * Found a valid triplet
                    triplets_found += 1

                    # ? Handle duplicates for arr[ptr1]
                    temp = ptr1 + 1
                    while temp < ptr2 and arr[ptr1] == arr[temp]:
                        triplets_found += 1
                        temp += 1

                    # Move pointers to avoid counting same triplet again
                    ptr2 -= 1

        return triplets_found
