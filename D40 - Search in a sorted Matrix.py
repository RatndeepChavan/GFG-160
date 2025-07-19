"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-matrix-1587115621

Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

Examples:

Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
Output: true
Explanation: 14 is present in the matrix, so output is true.
Input: mat[][] = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42
Output: false
Explanation: 42 is not present in the matrix.
Input: mat[][] = [[87, 96, 99], [101, 103, 111]], x = 101
Output: true
Explanation: 101 is present in the matrix.

Constraints:
1 <= n, m <= 1000
1 <= mat[i][j] <= 109
1 <= x <= 109
"""


class Solution:
    def searchMatrix(self, mat, x):
        """
        ? Approach:
        Treat the 2D matrix as a flattened 1D sorted array.
        Perform binary search from index 0 to (rows * cols - 1).
        Convert 1D index to 2D coordinates using:
            - row = index // total_cols
            - col = index % total_cols
        This allows binary search without explicitly flattening the matrix.

        Time Complexity: O(log(n * m))
        Space Complexity: O(1)
        """
        total_rows = len(mat)
        total_cols = len(mat[0])

        # Treat the matrix as a 1D sorted array from index 0 to (n*m - 1)
        low = 0
        high = (total_rows * total_cols) - 1

        while low <= high:
            mid = (low + high) // 2

            # Convert 1D index to 2D matrix coordinates
            row = mid // total_cols
            col = mid % total_cols
            element = mat[row][col]

            if element == x:
                return True  # Element found
            elif element > x:
                high = mid - 1
            else:
                low = mid + 1

        return False  # Element not found
