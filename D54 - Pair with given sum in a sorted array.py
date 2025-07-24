"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/pair-with-given-sum-in-a-sorted-array4940

You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes.

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 125.

Constraints:
-105 <= target <=105
2 <= arr.size() <= 105
-105 <= arr[i] <= 105
"""


class Solution:
    def countPairs(self, arr, target):
        """
        ✅ Approach:
        - Two-pointer technique on a sorted array.
        - Move pointers inward depending on the sum.
        - If a valid pair is found, handle duplicates on the left side only.

        ⏱️ Time: O(N)
        🧠 Space: O(1)
        """
        start = 0
        end = len(arr) - 1
        pairs_found = 0

        while start < end:
            addition = arr[start] + arr[end]

            if addition > target:
                # Need smaller sum → move right pointer left
                end -= 1
            elif addition < target:
                # Need larger sum → move left pointer right
                start += 1
            else:
                # Valid pair found
                pairs_found += 1

                # ! Check for duplicates on left side
                if arr[start] == arr[start + 1]:
                    temp = start + 1
                    while temp < end and arr[temp] == arr[start]:
                        pairs_found += 1
                        temp += 1

                end -= 1  # Move right pointer inward after processing

        return pairs_found


ans = Solution().countPairs([1, 2, 2, 2, 3], 5)
print(ans)
