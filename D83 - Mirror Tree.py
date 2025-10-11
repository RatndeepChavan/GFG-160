"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/mirror-tree

Given a binary tree, convert the binary tree to its Mirror tree.

Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.     

Examples:
Input: root[] = [1, 2, 3, N, N, 4]
Output: [1, 3, 2, N, 4]
Input: root[] = [1, 2, 3, 4, 5]
Output: [1, 3, 2, N, N, 5, 4]

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105
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
    def switch_left_right(self, node):
        """
        ? Recursive helper function to mirror a binary tree.

        This function performs a post-order traversal (Left, Right, Root) to swap the left and right children of each node.

        Args:
            node (Node): The current node in the binary tree.

        Returns:
            None: The function modifies the tree in-place.
            
        ✅ Approach:
            - **Base case:** If the node is `None`, there's nothing to do, so the function returns.
            - **Recursive step:** Recursively call `switch_left_right` on the left child and then on the right child.
            - **Swap:** After the subtrees have been mirrored, swap the left and right children of the current `node`.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes in the tree.
            - We visit each node exactly once.

        🧠 Space Complexity:
            - **O(H)**, where H is the height of the tree, for the recursion stack space.
            - In the worst case (a skewed tree), this can be **O(N)**.
            - In the average case (a balanced tree), it is **O(log N)**.
        """
        # Base case: if the node is null, we can't perform any operations on it.
        if not node:
            return
            
        # First, recursively call the function on the left and right children.
        # This ensures that we mirror the subtrees first (post-order traversal).
        self.switch_left_right(node.left)
        self.switch_left_right(node.right)
            
        # After the children have been processed, swap the left and right pointers of the current node.
        node.left, node.right = node.right, node.left

    def mirror(self, root):
        """
        ? Public method to mirror a binary tree.

        Args:
            root (Node): The root of the binary tree.

        Returns:
            None: The function modifies the tree in-place.
            
        ! Important:
            - This function serves as the entry point to the recursive helper function `switch_left_right`.
            - It performs the in-place mirroring of the entire tree.
        """
        # Call the recursive helper function to begin the mirroring process from the root.
        self.switch_left_right(root)