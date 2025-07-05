"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/merge-two-sorted-arrays-1587115620

Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10
Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.
Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.

Constraints:
1 <= a.size(), b.size() <= 105
0 <= a[i], b[i] <= 107
"""


class Solution:
    def mergeArrays(self, a, b):
        """
        Merges two sorted arrays 'a' and 'b' in-place without using extra space,
        such that after merging, both 'a' and 'b' are sorted and all elements of 'a' are <= all elements of 'b'.

        Time Complexity: O((n + m) log(n + m)) — due to sorting after swap
        Space Complexity: O(1) — no extra arrays used
        """

        i = len(a) - 1  # * Start from end of array 'a'
        j = 0  # * Start from beginning of array 'b'

        while i >= 0 and j < len(b):
            if a[i] > b[j]:
                # * Swap larger element in 'a' with smaller element in 'b'
                a[i], b[j] = b[j], a[i]
                j += 1
            i -= 1

        # * Final sort to restore full order within each array
        a.sort()
        b.sort()

        # ? Why sorting at the end?
        # Because swapping might break internal order of both arrays.
        # This ensures both arrays are individually sorted again.

        # ? Why does this work?
        # Because we guarantee that no element in 'a' is greater than the smallest element in 'b'
        # after the swaps — then we just sort within each.


class Solution:
    def mergeArrays(self, a, b):
        """
        Merges two sorted arrays 'a' and 'b' in-place without using extra space,
        such that after merging, both 'a' and 'b' are sorted and all elements of 'a' are <= all elements of 'b'.

        Time Complexity: O((n + m) log(n + m)) — due to sorting after swap
        Space Complexity: O(1) — no extra arrays used
        """

        i = len(a) - 1  # * Start from end of array 'a'
        j = 0  # * Start from beginning of array 'b'

        while i >= 0 and j < len(b):
            if a[i] > b[j]:
                # * Swap larger element in 'a' with smaller element in 'b'
                a[i], b[j] = b[j], a[i]
                j += 1
            i -= 1

        # * Final sort to restore full order within each array
        a.sort()
        b.sort()

        # ? Why sorting at the end?
        # Because swapping might break internal order of both arrays.
        # This ensures both arrays are individually sorted again.

        # ? Why does this work?
        # Because we guarantee that no element in 'a' is greater than the smallest element in 'b'
        # after the swaps — then we just sort within each.
