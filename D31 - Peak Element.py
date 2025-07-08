"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/peak-element

Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6].
Input: arr = [1, 2, 3]
Output: true
Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.

Constraints:
1 ≤ arr.size() ≤ 106
-231 ≤ arr[i] ≤ 231 - 1
"""


class Solution:
    def peakElement(self, arr):
        """
        Function to find the index of any one peak element in the array.

        A peak element is greater than its adjacent elements.
        - No two adjacent elements are equal.
        - The first and last elements are considered to be surrounded by -∞ (negative infinity).
        - There is always at least one peak.

        Approach:
        This problem uses a binary search based idea to find a peak in O(log n) time,
        even though the array is not sorted. This works because:
        - If an element is smaller than its left, the peak must lie to the left.
        - If an element is smaller than its right, the peak must lie to the right.
        - If it is greater than both neighbors, it is a peak.

        Key Insight:
        ➤ Sometimes even in unsorted arrays, divide-and-conquer logic can be applied by
          leveraging *local comparisons* between arr[mid-1], arr[mid], and arr[mid+1].

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        n = len(arr)

        # ! Edge Case 1: Only one element
        if n == 1:
            return 0

        # ! Edge Case 2: First element is a peak
        if arr[0] > arr[1]:
            return 0

        # ! Edge Case 3: Last element is a peak
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        # Binary Search in middle of the array
        low = 1
        high = n - 2

        while low <= high:
            mid = low + (high - low) // 2

            # ? Check if current element is a peak
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            # ? If decreasing slope, peak must be on the left side
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1

            # ? If increasing slope, peak lies on the right
            else:
                low = mid + 1

        # Fallback (technically never reached because problem guarantees a peak)
        return -1
