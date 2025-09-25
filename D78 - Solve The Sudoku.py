"""
Link :https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/solve-the-sudoku-1587115621

Given an incomplete Sudoku configuration in terms of a 9x9  2-D interger square matrix, mat[][], the task is to solve the Sudoku. It is guaranteed that the input Sudoku will have exactly one solution.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Note: Zeros represent blanks to be filled with numbers 1-9, while non-zero cells are fixed and cannot be changed.

Input:
3 0 6 5 0 8 4 0 0 
5 2 0 0 0 0 0 0 0 
0 8 7 0 0 0 0 3 1 
0 0 3 0 1 0 0 8 0 
9 0 0 8 6 3 0 0 5 
0 5 0 0 9 0 6 0 0 
1 3 0 0 0 0 2 5 0 
0 0 0 0 0 0 0 7 4 
0 0 5 2 0 6 3 0 0 

Output :
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9

Constraints:
mat.size() = 9
mat[i].size() = 9
0 ≤ mat[i][j] ≤ 9
"""

class Solution:
    def solveSudoku(self, mat):
        """
        ✅ Approach:
        Uses backtracking to solve the Sudoku puzzle. The algorithm searches for an
        empty cell (value 0), tries placing digits 1-9, and checks if the placement
        is valid:
        - No duplicate in the same row.
        - No duplicate in the same column.
        - No duplicate in the same 3x3 sub-grid.

        If the placement is valid, it places the digit and recursively attempts to
        solve the rest of the board. If stuck, it removes the digit (backtracks) and
        tries the next possible value.

        ✅ Plain English Explanation (Backtracking):
        Think of it like trial and error with memory:
        - Look for an empty cell on the board.
        - Try placing numbers 1 through 9 in it, one at a time.
        - If a number fits (no clashes in row, column, or 3x3 box), keep it there
            and move to the next empty cell.
        - If eventually stuck (no number fits), erase the last number placed and
            try a new one (backtracking).
        - Continue until the board is completely filled with valid numbers.

        ⏱️ Time Complexity:
        ~O(9^n) in the worst case (n = number of empty cells),
        since each empty cell can try 9 possibilities.

        🧠 Space Complexity:
        O(1) extra space (excluding recursion stack) — uses the board itself
        for in-place modifications.

        Args:
            mat (list[list[int]]): 9x9 Sudoku board with 0 for empty cells.

        Returns:
            bool: True if the board is solved, False if no solution exists.
        """

        def isValid(mat, row, col, val):
            """Check if placing `val` at (row, col) is valid."""
            # Check row & column
            for i in range(9):
                if mat[row][i] == val or mat[i][col] == val:
                    return False

            # * Find starting index of 3x3 sub-grid
            start_row = row - row % 3
            start_col = col - col % 3

            # Check 3x3 sub-grid
            for r in range(3):
                for c in range(3):
                    if mat[start_row + r][start_col + c] == val:
                        return False
            return True

        # Try filling the board
        for row in range(9):
            for col in range(9):
                if mat[row][col] == 0:
                    for i in range(1, 10):
                        if isValid(mat, row, col, i):
                            mat[row][col] = i
                            if self.solveSudoku(mat):
                                return True
                            # * Backtrack if stuck
                            mat[row][col] = 0
                    return False  # No valid number found for this cell
        return True  # * Puzzle solved

    @staticmethod
    def prettyPrint(board):
        """
        🖨️ Nicely displays the Sudoku board in a human-readable grid format.
        """
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Horizontal separator after every 3 rows
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")  # Vertical separator after every 3 cols
                print(board[i][j] if board[i][j] != 0 else ".", end=" ")
            print()

M = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

Solution().SolveSudoku(M)
print(M)
