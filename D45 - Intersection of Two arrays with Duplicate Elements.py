"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/intersection-of-two-arrays-with-duplicate-elements

Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both the arrays. The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing.

Examples:

Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
Output: [1, 3]
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.
Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
Output: [1]
Explanation: 1 is the only common element present in both the arrays.
Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
Output: []
Explanation: No common element in both the arrays.

Constraints:
1 ≤ a.size(), b.size() ≤ 105
0 ≤ a[i], b[i] ≤ 105
"""


class Solution:
    def intersect(self, a, b):
        """
        Returns the intersection of two lists as a set of unique common elements.

        ✅ Approach:
        - Convert first list `a` to a set for O(1) lookups
        - Traverse second list `b` and collect elements that exist in the first set
        - Use a result set to avoid duplicates

        ⏱️ Time: O(N + M), where N = len(a), M = len(b)
        🧠 Space: O(N), for the auxiliary set of list `a`
        """

        set_a = set(a)  # Enables fast lookups
        ans = set()  # Result set to store common elements

        for i in b:
            if i in set_a:
                ans.add(i)

        return ans
