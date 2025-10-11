"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/inorder-traversal

Given a Binary Tree, your task is to return its In-Order Traversal.

An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).

Follow Up: Try solving this with O(1) auxiliary space.

Examples:

Input: root[] = [1, 2, 3, 4, 5] 
Output: [4, 2, 5, 1, 3]

Input: root[] = [8, 1, 5, N, 7, 10, 6, N, 10, 6]
Output: [1, 7, 10, 8, 6, 10, 5, 6]

Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 105
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


from collections import deque

class Solution:
    def inOrder(self, root):
        """
        ? Performs an inorder traversal of a binary tree recursively.

        Args:
            root (Node): The root of the binary tree.

        Returns:
            list[int]: A list containing the inorder traversal of the tree.
            
        ✅ Approach (Recursive):
            - **Base case:** If the `root` is `None`, it's an empty subtree, so we return an empty list.
            - **Recursive step:**
                1. Recursively traverse the **left** subtree.
                2. Append the current node's **data**.
                3. Recursively traverse the **right** subtree.
            - The results from the recursive calls are combined to form the final inorder traversal list.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes in the tree.
            - Each node is visited exactly once.

        🧠 Space Complexity:
            - **O(H)** for the recursion stack space, where H is the height of the tree.
            - In the worst case (a skewed tree), this is **O(N)**.
        """
        if not root:
            # Base case: if the node is None, return an empty list.
            return []
            
        # Recursively traverse the left subtree
        result = self.inOrder(root.left)
        # Append the data of the current node
        result.append(root.data)
        # Recursively traverse the right subtree
        result += self.inOrder(root.right)
            
        return result

# ----------------------------------------------------------------------------------------------------------------------


class Solution_Iterative:
    def inOrder(self, root):
        """
        ? Performs an inorder traversal of a binary tree iteratively using a stack.

        Args:
            root (Node): The root of the binary tree.

        Returns:
            list[int]: A list containing the inorder traversal of the tree.
            
        ✅ Approach (Iterative with Stack):
            1. Initialize an empty stack and an empty `result` list.
            2. Start with the current node as the `root`.
            3. Use a loop that continues as long as the current node is not `None` or the stack is not empty.
            4. **Go Left:** While the `current` node is not `None`, push it onto the stack and move to its left child. This ensures we visit the leftmost node first.
            5. **Process Node:** Once we can't go left anymore, pop a node from the stack. This is the next node in the inorder sequence. Append its data to the `result` list.
            6. **Go Right:** Move to the right child of the popped node to continue the traversal.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes.
            - Each node is pushed and popped from the stack exactly once.

        🧠 Space Complexity:
            - **O(H)** for the stack, where H is the height of the tree.
            - In the worst case (a skewed tree), this is **O(N)**.
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Go as far left as possible, pushing nodes onto the stack.
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the last node from the stack (the leftmost unvisited node).
            current = stack.pop()
            # Process the node (inorder traversal).
            result.append(current.data)
            
            # Move to the right child to continue the traversal.
            current = current.right
            
        return result