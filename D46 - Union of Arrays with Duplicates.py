"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/union-of-two-arrays3538

You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

Examples:

Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.
Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]
Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.
Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1]
Output: [1, 2]
Explanation: Union set of both the arrays will be 1 and 2.

Constraints:
1 ≤ a.size(), b.size() ≤ 106
0 ≤ a[i], b[i] ≤ 105
"""


class Solution:
    def findUnion(self, a, b):
        """
        Returns the union of two lists as a set of unique elements.

        ✅ Approach:
        - Traverse both lists
        - Insert each element into a set (automatically handles uniqueness)

        ⏱️ Time: O(N + M), where N = len(a), M = len(b)
        🧠 Space: O(N + M), for the resulting union set
        """

        ans = set()  # Result set to store all unique elements

        # Add all elements from first list
        for i in a:
            ans.add(i)

        # Add all elements from second list
        for i in b:
            ans.add(i)

        return ans

"""
! BELOW SOLUTION MIGHT LOOK O(max(m,n)) BUT STILL O(m+n)
def findUnion(self, a, b):
        len_a = len(a)
        len_b = len(b)
        n = len_a if len_a > len_b else len_b
        ans = set()
        for idx in range(n):
            if idx < len_a: ans.add(a[idx])
            if idx < len_b: ans.add(b[idx])
        return ans

Even though one loop (for i in range(max(n, m))), still:
- Accessing every element of both arrays (a[i], b[i])
- Making a total of n + m insertions into the set
- So the overall work done is still O(n + m)
"""