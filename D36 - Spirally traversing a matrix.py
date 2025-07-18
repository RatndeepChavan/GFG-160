"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/spirally-traversing-a-matrix-1587115621

You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]

Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]

Constraints:
1 ≤ n, m ≤1000
0 ≤ mat[i][j] ≤100
"""


class Solution:
    def spirallyTraverse(self, mat):
        """
        Function to return a list of elements of the matrix in a spiral order.
        Unlike the standard top-left clockwise spiral, this solution starts from
        the center (or near-center) and moves outward, alternating horizontal
        and vertical passes.

        Approach:
        - Start from the center row/column and expand outwards by tracking how many
          rows and columns have been added (`added_rows`, `added_cols`).
        - Use a `left` flag to alternate between left-to-right / top-down
          vs right-to-left / bottom-up directions.
        - Supports even and odd dimension matrices.

        Time Complexity: O(m * n)  — each element is visited exactly once
        Space Complexity: O(m * n) extra space
        """

        result = []

        total_rows = len(mat)
        total_cols = len(mat[0])
        added_rows = 0
        added_cols = 0
        left = True  # ! Start with left

        while added_rows < total_rows and added_cols < total_cols:
            if left:
                col_idx = added_cols // 2

                # * Move left-to-right
                if added_rows == added_cols:
                    row_idx = added_rows // 2
                    result += mat[row_idx][col_idx : total_cols - col_idx]
                    added_rows += 1
                    left = False

                # * Move bottom-to-up
                else:
                    row_idx = (total_rows - 1) - (added_rows // 2)

                    # ? subtracting 1 to include top row in reverse range
                    limit = (added_rows // 2) - 1

                    for cur_row in range(row_idx, limit, -1):
                        result.append(mat[cur_row][col_idx])
                    added_cols += 1

            else:
                col_idx = (total_cols - 1) - (added_cols // 2)

                # * Move right-to-left
                if added_rows == added_cols:
                    row_idx = (total_rows - 1) - (added_rows // 2)
                    start = added_cols // 2

                    # ! can use slicing too but edge case if start == 0
                    result += reversed(mat[row_idx][start:col_idx])
                    added_rows += 1
                    left = True

                # * Move top-to-down
                else:
                    row_idx = added_rows // 2

                    # * Adding 1 to avoid duplicate entry of top-right value
                    for cur_row in range(row_idx + 1, total_rows - row_idx):
                        result.append(mat[cur_row][col_idx])
                    added_cols += 1

        return result


"""
! TRADITIONAL METHOD

def spirallyTraverse(mat):
    m, n = len(mat), len(mat[0])

    res = []

    # Initialize boundaries
    top, bottom, left, right = 0, m - 1, 0, n - 1

    # Iterate until all elements are printed
    while top <= bottom and left <= right:

        # Print top row from left to right
        for i in range(left, right + 1):
            res.append(mat[top][i])
        top += 1

        # Print right column from top to bottom
        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1

        # Print bottom row from right to left (if exists)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(mat[bottom][i])
            bottom -= 1

        # Print left column from bottom to top (if exists)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1

    return res
"""


"""

✅ LinkedIn Post:
🚀 Spiral Matrix — But with a Twist!

Today I explored a fascinating variation of the classic spiral traversal problem — instead of the usual top-left to outer spiral, I designed a solution that starts from the center of the matrix and expands outwards like a blooming flower 🌸.

📌 What's unique?

Traverses from center to edge, not edge to center

Dynamically tracks added rows & columns instead of fixed boundaries

Handles even & odd-sized matrices

Uses alternating row/column control for clean outward growth

✅ All test cases passed on GeeksforGeeks 💚
🧠 This approach may not be standard, but it was a great exercise in thinking beyond traditional patterns.

🔍 Check out the clean, well-documented solution on my GitHub:
[Insert GitHub Link]

If you've seen or built similar creative patterns in matrix problems — would love to discuss!

#Python #DSA #CodingChallenge #SpiralMatrix #GeeksForGeeks #CleanCode #DevJourney #ProblemSolving
"""
