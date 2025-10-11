"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/maximum-path-sum-from-any-node

Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Examples:
Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42

Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31

Constraints:
1 ≤ number of nodes ≤ 103
-104 ≤ node->data ≤ 104
"""

# Node Class:
class Node:
    """
    * Represents a node in a binary tree.
    """
    def __init__(self, val):
        """
        * Initializes a binary tree node.

        Args:
            val (int): The value/data stored in the node.
        """
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Initializes class variable to track the maximum path sum.
    max_sum = float("-inf")

    def get_sum(self, node):
        """
        ⚡ Recursively computes the maximum root-to-any-node path sum for a subtree.

        Args:
            node (Node): The current node in the binary tree.

        Returns:
            int: The maximum sum of a path starting at `node` and extending downwards.

        ✅ Approach:
            - **Base case:** If `node` is None → return `-∞` (to exclude it).
            - Recursively compute `left_sum` and `right_sum`.
            - Compute:
                - `subtree_sum`: Path passing through this node (node + left + right).
                - `current_sum`: Best downward path (node + max(left, right)).
                - `current_max_sum`: Best of `node alone` vs `current_sum`.
            - Update `self.max_sum` with the maximum of:
                - The global max so far,
                - `current_max_sum`,
                - `subtree_sum`.

        ⏱️ Time Complexity:
            - **O(N)**, where N = number of nodes in the tree.
            - Each node is processed once.

        🧠 Space Complexity:
            - **O(H)**, where H = height of the tree (recursion stack).
            - Worst case skewed tree → **O(N)**.
        """
        if not node:
            return float("-inf")

        left_sum = self.get_sum(node.left)
        right_sum = self.get_sum(node.right)

        subtree_sum = node.data + left_sum + right_sum
        current_sum = node.data + max(left_sum, right_sum, 0)

        # Update global maximum
        self.max_sum = max(self.max_sum, current_sum, subtree_sum)

        return current_sum

    def findMaxSum(self, root):
        """
        🌐 Finds the **maximum path sum** in a binary tree.

        A "path" is any sequence of nodes connected via parent-child relationships.
        It may start and end at any node (not necessarily the root or a leaf).

        Args:
            root (Node): The root of the binary tree.

        Returns:
            int: The maximum path sum across all possible paths in the tree.

        ✅ Approach:
            - Perform DFS with `get_sum` to explore all nodes.
            - Track global maximum path sum in `self.max_sum`.
            - Compare with potential root-centered paths (left + root + right).

        ⏱️ Time Complexity:
            - **O(N)**, since each node is visited once.

        🧠 Space Complexity:
            - **O(H)**, recursion depth (worst case skewed tree → O(N)).
        """
        if not root:
            return 0

        self.get_sum(root)  # populates self.max_sum

        return self.max_sum
