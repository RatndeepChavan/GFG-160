"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/lowest-common-ancestor-in-a-bst

Given a Binary Search Tree (with all values unique) and two nodes n1 and n2 (n1 != n2). You may assume that both nodes exist in the tree. Find the Lowest Common Ancestor (LCA) of the given two nodes in the BST.

LCA between two nodes n1 and n2 is defined as the lowest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

Examples:
Input: root = [5, 4, 6, 3, N, N, 7, N, N, N, 8], n1 = 7, n2 = 8
Output: 7
Explanation: 7 is the closest node to both 7 and 8, which is also an ancestor of both the nodes.

Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], n1 = 8, n2 = 14
Output: 8
Explanation: 8 is the closest node to both 8 and 14, which is also an ancestor of both the nodes.

Input: root = [2, 1, 3], n1 = 1, n2 = 3
Output: 2
Explanation: 2 is the closest node to both 1 and 3, which is also an ancestor of both the nodes.

Constraints:
1 <= number of nodes <= 105
1 <= node->data <= 105
1 <= n1, n2 <= 105
"""

# ----------------------------------------------------------------------------------------------------------------------
# Tree Node
# ----------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# ----------------------------------------------------------------------------------------------------------------------
# * Iterative Solution
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Iterative:
    def LCA(self, root, n1, n2):
        """
        ? Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST).

        Args:
            root (Node): The root of the BST.
            n1 (Node): First target node.
            n2 (Node): Second target node.

        Returns:
            Node: The lowest common ancestor node of n1 and n2.

        ✅ Approach (Iterative using BST properties):
            - In a BST:
                * All values in the left subtree < root.
                * All values in the right subtree > root.
            - So for nodes n1 and n2:
                1. If both n1 and n2 are smaller than root → LCA lies in the **left subtree**.
                2. If both n1 and n2 are greater than root → LCA lies in the **right subtree**.
                3. Otherwise → root is the split point → **root is the LCA**.

        ⏱️ Time Complexity:
            - O(H), where H is the height of the BST.
            - Worst case skewed BST → O(N).
            - Balanced BST → O(log N).

        🧠 Space Complexity:
            - O(1), since it’s iterative and doesn’t use recursion.
        """
        while root:
            # Both nodes lie in the right subtree
            if n1.data > root.data and n2.data > root.data:
                root = root.right
            # Both nodes lie in the left subtree
            elif n1.data < root.data and n2.data < root.data:
                root = root.left
            else:
                # Split point → this is the LCA
                return root


# ----------------------------------------------------------------------------------------------------------------------
# * Recursive Solution
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Recursive:
    def LCA(self, root, n1, n2):
        """
        ? Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST) recursively.

        Args:
            root (Node): The root of the BST.
            n1 (Node): First target node.
            n2 (Node): Second target node.

        Returns:
            Node: The lowest common ancestor node of n1 and n2.

        ✅ Approach (Recursive using BST properties):
            - Same idea as iterative:
                * If both nodes < root → search left subtree.
                * If both nodes > root → search right subtree.
                * Else → root is the LCA.

        ⏱️ Time Complexity:
            - O(H), where H is the height of the BST.
            - Worst case → O(N).
            - Balanced BST → O(log N).

        🧠 Space Complexity:
            - O(H) due to recursion stack.
        """
        if not root:
            return None

        # If both nodes lie in right subtree
        if n1.data > root.data and n2.data > root.data:
            return self.LCA(root.right, n1, n2)

        # If both nodes lie in left subtree
        elif n1.data < root.data and n2.data < root.data:
            return self.LCA(root.left, n1, n2)

        # Otherwise, this root is the split point → LCA
        return root
