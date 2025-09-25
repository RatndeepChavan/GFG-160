"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/word-search

You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.

Examples :

Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: true

The letter cells which are used to construct the "GEEK" are colored.
Input: mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: false

It is impossible to construct the string word from the mat using each cell only once.
Input: mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
Output: true
There are multiple ways to construct the word "AB".

Constraints:
1 ≤ n, m ≤ 6
1 ≤ L ≤ 15
mat and word consists of only lowercase and uppercase English letters.
"""

class Solution:
    def get_row_col_len(self, mat):
        """
        ? Utility function
        Returns the number of rows and columns in the matrix.
        """
        return len(mat), len(mat[0])
    
    def isWordExist(self, mat, word):
        """
        ✅ Approach:
            - Use DFS (Depth-First Search) with backtracking to find the word.
            - Start DFS from each cell that matches the first character.
            - Move in 4 directions: up, down, left, right.
            - Temporarily mark visited cells in-place with '#' to avoid revisiting in the same path.
            - Restore the cell after exploring all paths (backtracking).

        ⏱️ Time:
            - O(N * M * 4^L) worst case
                where N, M are matrix dimensions and L is the length of the word.
                Each cell can branch up to 4 directions per letter.

        🧠 Space:
            - O(L) recursion stack depth
            - No extra visited set (visited marking done in-place).

        ! Important:
            - Mutates the matrix temporarily during DFS.
            - Restores matrix state before returning from DFS.
        """
        # ? Edge case: Empty matrix
        if not mat or not mat[0]:
            return False

        row_len, col_len = self.get_row_col_len(mat)

        def dfs(r, c, idx):
            """
            ? DFS helper:
                r, c → current cell position
                idx  → current index in the word we are matching
            """
            # ✅ Base case: matched the whole word
            if idx == len(word):
                return True

            # ! Out of bounds check
            if r < 0 or c < 0 or r >= row_len or c >= col_len:
                return False

            # ! Character mismatch
            if mat[r][c] != word[idx]:
                return False

            # * Temporarily mark cell as visited
            temp, mat[r][c] = mat[r][c], "#"

            # * Explore all 4 directions
            found = (
                dfs(r - 1, c, idx + 1) or  # Up
                dfs(r + 1, c, idx + 1) or  # Down
                dfs(r, c - 1, idx + 1) or  # Left
                dfs(r, c + 1, idx + 1)     # Right
            )

            # * Restore the cell (backtracking)
            mat[r][c] = temp

            return found

        # * Try starting DFS from every cell in the matrix
        for row in range(row_len):
            for col in range(col_len):
                if dfs(row, col, 0):
                    return True

        return False
