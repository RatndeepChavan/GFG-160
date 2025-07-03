"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/inversion-of-array-1587115620

Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum.

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
"""


class Solution:
    swap_count = 0  # Class variable to track inversions

    def inversionCount(self, arr):
        """
        Counts the number of inversions in the array using merge sort logic.

        An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        
        def merge(left, right):
            i = j = 0
            result = []

            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    result.append(right[j])
                    j += 1
                    self.swap_count += (
                        len(left) - i
                    )  # All elements left in left[] are greater
                else:
                    result.append(left[i])
                    i += 1

            result += left[i:]
            result += right[j:]
            return result

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        merge_sort(arr)
        return self.swap_count
