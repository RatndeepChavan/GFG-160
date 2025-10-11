"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/diameter-of-binary-tree

Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:
Input: root[] = [1, 2, 3]
Output: 2
Input: root[] = [5, 8, 6, 3, 7, 9]
Output: 4

Constraints:
1 ≤ number of nodes ≤ 105
0 ≤ node->data ≤ 105
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
    # Class variable to store the maximum diameter found so far.
    max_diameter = 0
    
    def get_diameter(self, node):
        """
        ? Recursive helper function to find the diameter of the binary tree.

        Args:
            node (Node): The current node in the binary tree.

        Returns:
            int: The height of the subtree rooted at `node` (number of nodes in the longest path from the node to a leaf).
            
        ✅ Approach:
            - **Base case:** If the node is `None`, the height is 0.
            - **Recursive step:** Recursively call `get_diameter` on the left and right children to get their respective heights.
            - **Calculate Diameter:** The diameter passing through the current node is `left_ht + right_ht + 1` (number of nodes).
            - **Update:** Update the `max_diameter` class variable with the maximum diameter found so far.
            - **Return Height:** Return the height of the current subtree: `max(left_ht, right_ht) + 1` (number of nodes).

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes. Each node is visited once.

        🧠 Space Complexity:
            - **O(H)**, where H is the height of the tree, for the recursion stack space.
        """
        if not node:
            return 0
            
        left_ht = self.get_diameter(node.left)
        right_ht = self.get_diameter(node.right)
        
        current_diameter = left_ht + right_ht + 1
        
        self.max_diameter = max(self.max_diameter, current_diameter)
        
        return max(left_ht, right_ht) + 1
        
    def diameter(self, root):
        """
        ? Public method to find the diameter of a binary tree.

        Args:
            root (Node): The root of the binary tree.

        Returns:
            int: The diameter of the tree, measured in the number of edges.

        ! Important:
            - The `get_diameter` helper function calculates the diameter in terms of **nodes**.
            - The diameter in terms of **edges** is always `(number of nodes) - 1`.
            - We subtract 1 to convert the node count to an edge count, which is the standard definition of tree diameter.
        """
        self.max_diameter = 0
        self.get_diameter(root)
        
        # ? Why are we subtracting 1?
        # The `get_diameter` function calculates the length of the longest path in terms of the number of nodes.
        # For a path with `n` nodes, there are always `n-1` edges connecting them.
        # For example, a path with 5 nodes (A -> B -> C -> D -> E) has 4 edges.
        # Therefore, we subtract 1 from the node count to get the edge count.
        
        return self.max_diameter - 1


# ----------------------------------------------------------------------------------------------------------------------


class Solution_Iterative:
    def diameter(self, root):
        """
        ? Iterative solution to find the diameter of a binary tree using a post-order traversal with a stack.

        Args:
            root (Node): The root of the binary tree.

        Returns:
            int: The diameter of the tree (number of nodes).

        ✅ Approach:
            - We use a dictionary `heights` to store the computed height of each node to avoid re-computation.
            - A stack is used for the iterative post-order traversal. We push nodes onto the stack and process them after their children are visited.
            - We pop nodes from the stack, and if their children are already processed (their heights are in the `heights` dictionary), we calculate the height and diameter for the current node.
            - We update `max_diameter` whenever a new diameter is calculated.

        ⏱️ Time Complexity:
            - O(N), where N is the number of nodes.
            - Each node is pushed and popped from the stack once.

        🧠 Space Complexity:
            - O(N) in the worst case (skewed tree) for the stack and the `heights` dictionary.
            - In the average case (balanced tree), it is O(log N).
        """
        if not root:
            return 0

        stack = [root]
        heights = {None: 0}
        max_diameter = 0
        visited = set()

        while stack:
            node = stack[-1]

            # Post-order traversal logic
            if node.left and node.left not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                # Process the node after both children have been visited
                stack.pop()
                visited.add(node)
                
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                current_diameter = left_height + right_height + 1
                max_diameter = max(max_diameter, current_diameter)
                
                heights[node] = max(left_height, right_height) + 1
        
        return max_diameter
