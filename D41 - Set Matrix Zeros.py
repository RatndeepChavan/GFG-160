"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/set-matrix-zeroes

You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.

Explanation: mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.
Constraints:
1 ≤ n, m ≤ 500
- 231 ≤ mat[i][j] ≤ 231 - 1
"""


class Solution:
    def setMatrixZeroes(self, mat):
        """
        Modifies the input matrix in-place:
        If any cell in the matrix is 0, its entire row and column are set to 0.

        ✅ Approach:
        - Use the first row and first column as markers to track which rows/columns need to be zeroed.
        - To avoid corrupting marker data, separately track whether the 0th row or 0th column should be zeroed.
        - After marking, zero out necessary rows and columns based on the markers.
        - Finally, zero out the first row and column if required.

        Time: O(N * M), where N = no. of rows, M = no. of columns
        Space: O(1), in-place without extra space
        """

        total_rows = len(mat)
        total_cols = len(mat[0])

        # Flags to track if the first row or first column need to be zeroed
        zeroth_row = False
        zeroth_col = False

        # * Check if first column contains any zero
        for row in range(total_rows):
            if mat[row][0] == 0:
                zeroth_col = True
                break

        # * Check if first row contains any zero
        for col in range(total_cols):
            if mat[0][col] == 0:
                zeroth_row = True
                break

        # Use the first row and first column as marker storage
        for row in range(1, total_rows):
            for col in range(1, total_cols):
                if mat[row][col] == 0:
                    mat[0][col] = 0  # Mark the column
                    mat[row][0] = 0  # Mark the row

        # Zero out rows based on markers in the first column
        for row in range(1, total_rows):
            if mat[row][0] == 0:
                for col in range(1, total_cols):
                    mat[row][col] = 0

        # Zero out columns based on markers in the first row
        for col in range(1, total_cols):
            if mat[0][col] == 0:
                for row in range(1, total_rows):
                    mat[row][col] = 0

        # Zero out the first column if flagged
        if zeroth_col:
            for row in range(total_rows):
                mat[row][0] = 0

        # Zero out the first row if flagged
        if zeroth_row:
            for col in range(total_cols):
                mat[0][col] = 0
