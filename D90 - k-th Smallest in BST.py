"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/find-k-th-smallest-element-in-bst

Given a BST and an integer k, the task is to find the kth smallest element in the BST. If there is no kth smallest element present then return -1.

Examples:
Input: root = [2, 1, 3], k = 2
Output: 2
Explanation: 2 is the 2nd smallest element in the BST.

Input: root = [2, 1, 3], k = 5
Output: -1
Explanation: There is no 5th smallest element in the BST as the size of BST is 3.

Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 3
Output: 10
Explanation: 10 is the 3rd smallest element in the BST.

Constraints:
1 <= number of nodes, k <= 105
1 <= node->data <= 105
"""

# ----------------------------------------------------------------------------------------------------------------------
# Node Class
# ----------------------------------------------------------------------------------------------------------------------

class Node:
    """
    * Represents a node in a binary search tree.
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
# * Solution 1: Recursive Inorder Traversal
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Recursive:
    def kthSmallest(self, root, k):
        """
        ? Finds the kth smallest element in a BST using recursive inorder traversal.

        ✅ Approach:
            - Perform an inorder traversal (Left → Root → Right).
            - Maintain a counter for how many nodes have been visited.
            - When the counter reaches k, return the current node's value.

        ⏱️ Time Complexity:
            - **O(H + k)** → in the worst case O(N).
            - Stops early once the kth element is found.

        🧠 Space Complexity:
            - **O(H)** recursion stack, where H = tree height.
        """
        self.count = 0
        self.result = -1

        def inorder(node):
            if not node or self.result != -1:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.data
                return
            inorder(node.right)

        inorder(root)
        return self.result


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 2: Iterative Inorder Traversal (Stack)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Iterative:
    def kthSmallest(self, root, k):
        """
        ? Finds the kth smallest element in a BST using iterative inorder traversal with a stack.

        ✅ Approach:
            - Use a stack to simulate recursion.
            - Push all left nodes, then process root, then go right.
            - Decrement k for each visited node.
            - When k == 0, return the current node's value.

        ⏱️ Time Complexity:
            - **O(H + k)**, worst case O(N).

        🧠 Space Complexity:
            - **O(H)** for the stack.
        """
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.data

            current = current.right

        return -1  # Not found


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 3: Morris Inorder Traversal (O(1) Space)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Morris:
    def kthSmallest(self, root, k):
        """
        ? Finds the kth smallest element in a BST using Morris traversal.

        ✅ How Morris Traversal Works (Quick Recap):
            - Avoids stack/recursion by creating temporary "threads" from inorder predecessor to current node.
            - Visit nodes in inorder without extra memory.
            - Remove the thread after visiting (restores tree).

        ✅ Approach:
            - Traverse inorder using Morris technique.
            - Keep a counter for visited nodes.
            - When counter == k, return node’s value.

        ⏱️ Time Complexity:
            - **O(N)** in worst case (each node visited at most twice).

        🧠 Space Complexity:
            - **O(1)** → no recursion, no stack.
        """
        count = 0
        current = root

        def findPredecessor(node):
            pred = node.left
            while pred.right and pred.right is not node:
                pred = pred.right
            return pred

        while current:
            if current.left:
                pred = findPredecessor(current)
                if not pred.right:
                    # Create thread and move left
                    pred.right = current
                    current = current.left
                else:
                    # Remove thread and visit node
                    pred.right = None
                    count += 1
                    if count == k:
                        return current.data
                    current = current.right
            else:
                # Visit node with no left child
                count += 1
                if count == k:
                    return current.data
                current = current.right

        return -1  # If k > number of nodes
