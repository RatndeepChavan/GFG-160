"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-row-wise-sorted-matrix

Given a row-wise sorted 2D matrix mat[][] of size n x m and an integer x, find whether element x is present in the matrix.
Note: In a row-wise sorted matrix, each row is sorted in itself, i.e. for any i, j within bounds, mat[i][j] <= mat[i][j+1].

Examples :

Input: mat[][] = [[3, 4, 9],[2, 5, 6],[9, 25, 27]], x = 9
Output: true
Explanation: 9 is present in the matrix, so the output is true.
Input: mat[][] = [[19, 22, 27, 38, 55, 67]], x = 56
Output: false
Explanation: 56 is not present in the matrix, so the output is false.
Input: mat[][] = [[1, 2, 9],[65, 69, 75]], x = 91
Output: false
Explanation: 91 is not present in the matrix.

Constraints:
1 <= n, m <= 1000
1 <= mat[i][j] <= 105
1 <= x <= 105
"""


class Solution:

    def searchRowMatrix(self, mat, x):
        """
        ! Approach:
        - Iterate through each row.
        - Since each row is sorted, perform binary search within the row.
        - If any row contains the value, return True.

        ✅ Time Complexity: O(m * log n)
           where m = number of rows, n = number of columns
           (since we do binary search in each row)
        ✅ Space Complexity: O(1)

        ? Example:
          Input: mat = [[1, 4, 7], [8, 9, 11], [13, 14, 17]], x = 9
          Output: True
        """

        total_rows = len(mat)
        total_cols = len(mat[0])

        for row in range(total_rows):
            low = 0
            high = total_cols - 1

            while low <= high:
                mid = (low + high) // 2
                mat_element = mat[row][mid]

                if mat_element == x:
                    return True  # Found the element
                elif mat_element > x:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1  # Search right

        return False  # Element not found
