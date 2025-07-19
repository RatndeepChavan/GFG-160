"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/rotate-by-90-degree-1587115621

Rotate by 90 degree
Difficulty: EasyAccuracy: 56.88%Submissions: 122K+Points: 2Average Time: 20m
Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.

Examples:

Input: mat[][] = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
Output: [[2, 5, 8],
        [1, 4, 7],
        [0, 3, 6]]
Input: mat[][] = [[1, 2],
                [3, 4]]
Output: [[2, 4],
        [1, 3]]

Constraints:
1 ≤ n ≤ 102
0 ≤ mat[i][j] ≤ 103
"""


class Solution:
    def rotateMatrix(self, mat):
        """
        Rotates a square matrix by 90 degrees anti-clockwise in-place.

        This function performs a layer-by-layer rotation, swapping elements
        from the outermost layer toward the center, rotating 4 corresponding
        elements at a time.

        Time Complexity: O(n^2) - Each element is touched once.
        Space Complexity: O(1) - No extra space used, rotation is in-place.

        :param mat: List[List[int]] - 2D square matrix to be rotated
        """
        n - len(mat[0])
        last_idx = n - 1  # Last index in row/col
        limit = (n // 2) + 1  # adding 1 to include middle layer in range

        for row in range(limit):
            for col in range(row, last_idx - row):
                # ? Performing a 4-way swap between:
                # top → left → bottom → right → top
                # Storing top-left value and rotating anti-clockwise

                # Top-left ↔ Bottom-left
                mat[row][col], mat[last_idx - col][row] = (
                    mat[last_idx - col][row],
                    mat[row][col],
                )

                # New Top-left ↔ Bottom-right
                mat[row][col], mat[last_idx - row][last_idx - col] = (
                    mat[last_idx - row][last_idx - col],
                    mat[row][col],
                )

                # New Top-left ↔ Top-right
                mat[row][col], mat[col][last_idx - row] = (
                    mat[col][last_idx - row],
                    mat[row][col],
                )


"""
! VERY SHORT VERSION
* Reversing Rows and Transposing - O(n^2) Time and O(1) Space

def rotateMatrix(mat):
    n = len(mat)
    
    # Reverse each row
    for row in mat:
        row.reverse()

    # Performing Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

"""
