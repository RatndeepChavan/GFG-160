"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/check-for-bst

Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Examples:
Input: root = [2, 1, 3, N, N, N, 5]
Output: true 
Explanation: The left subtree of every node contains smaller keys and right subtree of every node contains greater keys. Hence, the tree is a BST.

Input: root = [2, N, 7, N, 6, N, 9] 
Output: false 
Explanation: Since the node to the right of node with key 7 has lesser key value, hence it is not a valid BST.

Input: root = [10, 5, 20, N, N, 9, 25]
Output: false
Explanation: The node with key 9 present in the right subtree has lesser key value than root node.

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 109
"""

# ----------------------------------------------------------------------------------------------------------------------
# Node Class
# ----------------------------------------------------------------------------------------------------------------------

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


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 1: Recursive (DFS with value range check)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Recursive:
    def isBST(self, root):
        """
        ? Checks whether a binary tree is a valid BST using recursion.

        ✅ Approach:
            - A node must always lie within a valid value range.
            - For the root, range = (-∞, +∞).
            - For the left child: new upper bound = root.data - 1.
            - For the right child: new lower bound = root.data + 1.
            - Recursively verify each node falls inside its valid range.

        ⏱️ Time Complexity:
            - **O(N)** — Each node is visited once.

        🧠 Space Complexity:
            - **O(H)** — Recursion stack, where H is the height of the tree.
            - **O(N)** — Worst case (skewed tree).
        """

        def _validate(node, low, high):
            if not node:  # Empty subtree is valid
                return True
            if not (low < node.data < high):  # Node violates BST property
                return False
            # Left must be < current node, right must be > current node
            return _validate(node.left, low, node.data) and _validate(node.right, node.data, high)

        return _validate(root, float("-inf"), float("inf"))


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 2: Iterative Inorder Traversal (Stack-based)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Iterative:
    def isBST(self, root):
        """
        ? Checks whether a binary tree is a valid BST using iterative inorder traversal.

        ✅ Approach:
            - Perform inorder traversal with a stack.
            - Inorder traversal of a BST must yield strictly increasing values.
            - Keep track of the previous visited node (`prev`).
            - If we ever encounter a value <= prev, it's not a BST.

        ⏱️ Time Complexity:
            - **O(N)** — Each node is processed once.

        🧠 Space Complexity:
            - **O(H)** — Stack space, where H = tree height.
            - **O(N)** — Worst case (skewed tree).
        """
        stack = []
        prev = float("-inf")
        current = root

        while stack or current:
            # Go left as far as possible
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()
            if current.data <= prev:  # Check BST property
                return False
            prev = current.data

            # Move to right subtree
            current = current.right

        return True


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 3: Morris Inorder Traversal (O(1) space)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Morris:
    def isBST(self, root):
        """
        ? Checks whether a binary tree is a valid BST using Morris Traversal.
    
        ✅ Morris Traversal:
            - Normally, inorder traversal requires recursion or a stack → **O(H)** space.
            - Morris traversal reuses unused **right child pointers** in the tree:
                ? If a node has a left child:
                    - Find its inorder predecessor (rightmost node in left subtree).
                    - Temporarily link predecessor’s right → current node (a "thread").
                    - Move left.
                ? When we return via that link:
                    - Remove the temporary link (restore tree).
                    - Process the current node, then go right.
                - If no left child, just process the node and go right.
            - This avoids recursion/stack, achieving **O(1) extra space**.
            - This also call threaded binary tree as it joins the nodes by temporary threads.


        ✅ Approach:
            - Traverse the tree in inorder fashion.
            - Keep track of the previous visited node value (`prev`).
            - If we find `current.data <= prev`, return False.
            - Restore tree structure after each visit.

        ⏱️ Time Complexity:
            - **O(N)** — Each node visited at most twice.

        🧠 Space Complexity:
            - **O(1)** — Constant extra space (no recursion, no stack).
        """
        prev = float("-inf")
        current = root

        while current:
            if current.left:
                # Find inorder predecessor (rightmost in left subtree)
                pred = current.left
                while pred.right and pred.right != current:
                    pred = pred.right

                if not pred.right:  # First visit → create thread
                    pred.right = current
                    current = current.left
                else:  # Thread exists → remove it and visit node
                    pred.right = None
                    if current.data <= prev:  # BST violation
                        return False
                    prev = current.data
                    current = current.right
            else:
                # Visit node with no left child
                if current.data <= prev:  # BST violation
                    return False
                prev = current.data
                current = current.right

        return True
