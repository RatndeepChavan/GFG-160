"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/search-in-a-rotated-array4618

Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.

Examples :

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is found at index 8.
Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6.
Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1.

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
0 ≤ key ≤ 106
"""


class Solution:
    def search(self, arr, target):
        """
        Function to search for a target in a rotated sorted array of distinct integers.

        Approach:
        Use binary search while identifying which half is sorted, and narrow search accordingly.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        n = len(arr)

        # ! Edge case : Single-element array
        if n == 1:
            return 0 if arr[0] == target else -1

        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid

            # Left half is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1  # Target not found
