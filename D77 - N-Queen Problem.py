"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/n-queen-problem0315


The n-queens puzzle is the problem of placing n queens on a (n x n) chessboard such that no two queens can attack each other. Note that two queens attack each other if they are placed on the same row, the same column, or the same diagonal.

Given an integer n, find all distinct solutions to the n-queens puzzle.
You can return your answer in any order but each solution should represent a distinct board configuration of the queen placements, where the solutions are represented as permutations of [1, 2, 3, ..., n]. In this representation, the number in the ith position denotes the row in which the queen is placed in the ith column.
For eg. below figure represents a chessboard [3 1 4 2].


Examples:

Input: n = 1
Output: [1]
Explaination: Only one queen can be placed in the single cell available.
Input: n = 4
Output: [[2 4 1 3 ] [3 1 4 2 ]]
Explaination: There are 2 possible solutions for n = 4.
Input: n = 2
Output: []
Explaination: There are no possible solutions for n = 2.

Constraints:
1 ≤ n ≤ 10

Expected Complexities
Time Complexity: O(n!)
Auxiliary Space: O(n^2)
"""


class Solution:
    def nQueen(self, n):
        """
        ✅ Approach:
        Solves the N-Queens problem using backtracking. The idea is to place a queen
        on each row such that no two queens attack each other — i.e., they must not share
        the same column, positive diagonal, or negative diagonal.

        We keep track of:
        - cols: columns that already have queens.
        - positive_diagonal: where row + col is the same (↘ direction).
        - negative_diagonal: where row - col is the same (↙ direction).

        At each row, we try placing the queen in every column that is not under attack.
        If it's valid, we place it and recurse to the next row. When we reach row == n,
        we've placed all queens safely and save the current configuration.

        ⏱️ Time Complexity:
        O(n!) — because there are n options for the first row, (n-1) for the second, etc.
        It!s not exactly n! due to pruning invalid branches early, but worst case is close.

        🧠 Space Complexity:
        O(n) — for the recursion stack and hash sets used.

        Returns:
            A list of valid column placements for each row. Each solution is represented
            as a list of column indices, where the index in the list represents the row.
        """
        ans = []
        col_list = []
        cols = set()
        positive_diagonal = set()
        negative_diagonal = set()

        def backtrack(row):
            if row == n:
                # 1-based index conversion
                ans.append([i + 1 for i in col_list])
                return

            for col in range(n):
                # Check is current column is safe vertically and diagonally to place queen
                if (
                    (col in cols)
                    or ((row + col) in positive_diagonal)
                    or ((row - col) in negative_diagonal)
                ):
                    continue

                # Column Safe : Place queen
                col_list.append(col)
                cols.add(col)
                positive_diagonal.add(row + col)
                negative_diagonal.add(row - col)

                # Place next queen in next row
                backtrack(row + 1)

                # * Backtrack
                # ? change the position of previously placed queen
                col_list.pop()
                cols.remove(col)
                positive_diagonal.remove(row + col)
                negative_diagonal.remove(row - col)

        backtrack(0)
        return ans
