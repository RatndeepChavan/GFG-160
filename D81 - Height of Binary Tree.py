"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/height-of-binary-tree

Given a binary tree, find its height.

The height of a tree is defined as the number of edges on the longest path from the root to a leaf node. A leaf node is a node that does not have any children.

Examples:
Input: root[] = [12, 8, 18, 5, 11] 
Output: 2
Input: root[] = [1, 2, 3, 4, N, N, 5, N, N, 6, 7]  
Output: 3

Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 105
"""

# Node Class:
class Node:
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
    def get_height(self, node):
        """
        ? Recursive helper to calculate height in terms of nodes

        Args:
            node (Node): Current node in the binary tree.

        Returns:
            int: Height of subtree rooted at `node` (number of nodes in longest path).
            
        ✅ Approach:
            - Base case: If node is None, height is 0.
            - Recursively compute height of left and right subtrees.
            - Height of current node = 1 + max(left subtree height, right subtree height).

        ⏱️ Time Complexity:
            - O(N), where N is the number of nodes.
            - Each node is visited exactly once.

        🧠 Space Complexity:
            - O(H) recursion stack space, where H is the height of the tree.
            - Worst case O(N) for skewed tree, average O(log N) for balanced tree.
        """
        if not node:
            return 0

        left_ht = self.get_height(node.left)
        right_ht = self.get_height(node.right)

        return 1 + max(left_ht, right_ht)

    def height(self, root):
        """
        ? Public method to find height of binary tree in terms of edges.

        Args:
            root (Node): Root of the binary tree.

        Returns:
            int: Height of the tree measured in edges.
            
        ! Important:
            - Height in edges = height in nodes - 1
            - For empty tree, height should be 0 (not -1).
        """
        ht_nodes = self.get_height(root)
        return ht_nodes - 1 if ht_nodes > 0 else 0


# ! BFS (Level Order) Approach to Calculate Height
from collections import deque

class Solution:
    def height_bfs(self, root):
        """
        ? Calculates height of binary tree using BFS (level order traversal).

        Args:
            root (Node): Root of the binary tree.

        Returns:
            int: Height of the tree measured in edges.

        ✅ Approach:
            - Use a queue to traverse level-by-level.
            - Each iteration processes one level.
            - Increment height count after processing each level.
            - Height (in edges) = number of levels - 1.

        ⏱️ Time Complexity:
            - O(N), visits each node once.

        🧠 Space Complexity:
            - O(W), where W is the maximum width of the tree (max nodes at a level).
        """
        if not root:
            return 0
        
        queue = deque([root])
        height = 0
        
        while queue:
            level_size = len(queue)
            
            # Process current level
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            height += 1  # Finished processing one level
        
        # Height in edges = levels - 1
        return height - 1

# ! Iterative DFS Approach Using Stack
class Solution:
    def height_dfs_iterative(self, root):
        """
        ? Calculates height of binary tree using iterative DFS with a stack.

        Args:
            root (Node): Root of the binary tree.

        Returns:
            int: Height of the tree measured in edges.

        ✅ Approach:
            - Use a stack to simulate DFS.
            - Store tuples of (node, current_depth).
            - Track max depth seen during traversal.
            - Return max depth - 1 for edges.

        ⏱️ Time Complexity:
            - O(N), visits each node once.

        🧠 Space Complexity:
            - O(H), where H is tree height (max stack size).
        """
        if not root:
            return 0

        stack = [(root, 1)]  # Node with depth = 1 (nodes count)
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                # Push children with depth + 1
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))

        return max_depth - 1
