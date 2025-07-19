"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-matrix17201720

Given a 2D integer matrix mat[][] of size n x m, where every row and column is sorted in increasing order and a number x, the task is to find whether element x is present in the matrix.

Examples:

Input: mat[][] = [[3, 30, 38],[20, 52, 54],[35, 60, 69]], x = 62
Output: false
Explanation: 62 is not present in the matrix, so output is false.
Input: mat[][] = [[18, 21, 27],[38, 55, 67]], x = 55
Output: true
Explanation: 55 is present in the matrix.
Input: mat[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]], x = 3
Output: true
Explanation: 3 is present in the matrix.

Constraints:
1 <= n, m <=1000
1 <= mat[i][j] <= 109
1<= x <= 109
"""


class Solution:
    def matSearch(self, mat, x):
        """
        ! Approach:
        - Start from the **top-right corner** of the matrix.
        - At each step:
            - If the current element is equal to x → return True.
            - If it's greater than x → move left (decrement col).
            - If it's less than x → move down (increment row).
        - This leverages the fact that rows and columns are sorted.

        ✅ Time Complexity: O(m + n)
           where m is number of rows, and n is number of columns.
        ✅ Space Complexity: O(1) — no extra space used.

        ? Why start from top-right?
        - From top-right:
        - moving left gives smaller values,
        - moving down gives larger values.
        - This allows us to eliminate either a row or a column at each step.
        """

        # Start at top-right corner
        row_idx = 0
        col_idx = len(mat[0]) - 1

        while row_idx < len(mat) and col_idx >= 0:
            element = mat[row_idx][col_idx]

            if element == x:
                return True  # x found
            elif element > x:
                col_idx -= 1  # Move left to smaller elements
            else:
                row_idx += 1  # Move down to larger elements

        return False  # x not found


# ! lower-left start (alternative strategy)


class Solution:
    def matSearch(self, mat, x):
        # Start at bottom-left
        row_idx = len(mat) - 1
        col_idx = 0

        while row_idx >= 0 and col_idx < len(mat[0]):
            element = mat[row_idx][col_idx]

            if element == x:
                return True
            elif element > x:
                row_idx -= 1
            else:
                col_idx += 1

        return False
