"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/allocate-minimum-number-of-pages0937


You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:
    - Each student gets at least one book.
    - Each student is assigned a contiguous sequence of books.
    - No book is assigned to more than one student.

The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
[12] and [34, 67, 90] Maximum Pages = 191
[12, 34] and [67, 90] Maximum Pages = 157
[12, 34, 67] and [90] Maximum Pages = 113.
Therefore, the minimum of these cases is 113, which is selected as the output.
Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Allocation can not be done.
Input: arr[] = [22, 23, 67], k = 1
Output: 112

Constraints:
1 <=  arr.size() <= 106
1 <= arr[i] <= 103
1 <= k <= 103
"""


class Solution:
    """
    Approach:
    - Use Binary Search on the answer space (range of possible page limits).
    - For a given page limit, use a greedy check to see if allocation to `k` students is possible.
    - Minimize the maximum page count using this approach.

    Time Complexity:
    - O(n log(sum(arr) - max(arr)))
        where:
            - n = length of arr
            - low = max(arr) (minimum page limit we can assign)
            - high = sum(arr) (maximum possible page assignment)
        - Greedy check is O(n) and binary search runs log(high - low) times.

    Space Complexity: O(1) — No extra space used apart from variables.
    """

    @staticmethod
    def canAllocate(pagesArr, totalStudents, pageLimit):
        """
        Greedy check to determine whether the current `pageLimit` is sufficient
        to allocate books to `totalStudents` without breaking the contiguous constraint.
        """
        allocatedStudents = 1
        currentSum = 0

        for pages in pagesArr:
            currentSum += pages

            if currentSum > pageLimit:
                allocatedStudents += 1
                currentSum = pages

        return allocatedStudents <= totalStudents

    def findPages(self, arr, k):
        """
        Binary search on the minimum possible value of the maximum number of pages
        assigned to a student.
        """
        n = len(arr)

        # ! Not enough books to assign at least one to each student
        if k > n:
            return -1

        low = max(arr)  # No student can receive less than the largest book
        high = sum(arr)
        minPages = high

        # ! Each student gets exactly one book so largest value are maximum pages
        if k == n:
            return low

        while low <= high:
            mid = (high + low) // 2

            if self.canAllocate(arr, k, mid):
                minPages = min(mid, minPages)
                high = mid - 1  # Try to minimize further
            else:
                low = mid + 1  # Increase limit to allow valid allocation

        return minPages
