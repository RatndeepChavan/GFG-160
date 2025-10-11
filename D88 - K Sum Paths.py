"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/k-sum-paths

Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).

Constraints:
1 ≤ number of nodes ≤ 104
-100 ≤ node value ≤ 100
-109 ≤ k ≤ 109
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
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        """
        * Initializes the Solution class with a counter for valid paths.
        """
        self.path_counts = 0

    def find_paths(self, prefix_sum, prev_sum, node, k):
        """
        🔎 Recursively explores all paths and counts the ones that sum to `k`.

        Args:
            prefix_sum (dict): A hashmap storing prefix sums and their frequency.
            prev_sum (int): The cumulative sum from the root to the parent node.
            node (Node): The current node being processed.
            k (int): The target sum.

        ✅ Approach (Prefix-Sum with DFS):
            - Each path sum from the root to the current node is `current_sum`.
            - To form a valid path ending at the current node:
                - We need a previous prefix sum such that:
                    `current_sum - prefix_sum = k`
                    ? If at some point `current_sum = sum_x + k` and we have already seen `sum_x` earlier in the path (stored in hashmap), then the subpath between those points must sum to `k`.
            - Use a hashmap (`prefix_sum`) to track how many times each prefix occurred.
            - Update the hashmap before exploring children, and backtrack after.

        Steps:
        1. Base case → If node is `None`, return.
        2. Compute `current_sum = prev_sum + node.data`.
        3. Check if `(current_sum - k)` exists in hashmap → add its frequency to `path_counts`.
        4. Update `prefix_sum[current_sum] += 1`.
        5. Recurse for left and right children.
        6. Backtrack: decrement `prefix_sum[current_sum]`.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes.
            - Each node is processed once.

        🧠 Space Complexity:
            - **O(H)** for recursion stack (H = height of tree).
            - **O(N)** for hashmap in the worst case (skewed tree with unique prefix sums).
        """
        if not node:
            return

        # Cumulative sum from root to this node
        current_sum = prev_sum + node.data

        # If we have seen (current_sum - k) before → a path with sum = k exists
        required_sum = current_sum - k

        # Count how many times the required prefix sum occurred
        self.path_counts += prefix_sum.get(required_sum, 0)

        # Update current sum in prefix map
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        # Recurse down left and right subtrees
        self.find_paths(prefix_sum, current_sum, node.left, k)
        self.find_paths(prefix_sum, current_sum, node.right, k)

        # Backtrack: remove current_sum count
        prefix_sum[current_sum] -= 1

    def sumK(self, root, k):
        """
        🌐 Counts all paths in the binary tree that sum to `k`.

        Args:
            root (Node): The root of the binary tree.
            k (int): The target path sum.

        Returns:
            int: Total number of valid paths with sum = k.

        ✅ Approach:
            - Initialize prefix sum map with {0:1} (base case for exact match).
            - Call DFS (`find_paths`) to explore all nodes.
            - Return accumulated count.

        ⏱️ Time Complexity:
            - **O(N)** → DFS visits each node once.

        🧠 Space Complexity:
            - **O(N)** → Hashmap + recursion stack.
        """
        prefix_sum = {0: 1}
        self.find_paths(prefix_sum, 0, root, k)
        return self.path_counts
