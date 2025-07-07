"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/minimum-element-in-a-sorted-and-rotated-array3611

A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it.

Examples:

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array.
Input: arr[] = [3, 1, 2]
Output: 1
Explanation: Here 1 is the minimum element.
Input: arr[] = [4, 2, 3]
Output: 2
Explanation: Here 2 is the minimum element.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109
"""


class Solution:
    def findMin(self, arr):
        """
        Function to find the minimum element in a rotated sorted array of distinct elements.

        Approach:
        Use Binary Search to find the inflection point where arr[mid] is less than both neighbors.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        n = len(arr)

        # ! Edge case : If array has only one element
        if n == 1:
            return arr[0]

        # ! Edge case : If array is already sorted
        if arr[0] < arr[-1]:
            return arr[0]

        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            # previous and next index of mid index
            prev = -1 if mid == 0 else mid - 1
            nxt = 0 if mid == n - 1 else mid + 1

            if arr[mid] < arr[prev] and arr[mid] < arr[nxt]:
                return arr[mid]

            # NOTE: If arr[mid] > arr[high], min lies in right half
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid - 1
