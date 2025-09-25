"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/level-order-traversal

Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.

Examples:

Input: root[] = [1, 2, 3]
    1
   / \
  2   3
Output: [[1], [2, 3]]
Explanation: We start with the root node 1, so the first level of the traversal is [1]. Then we move to its children 2 and 3, which form the next level, giving the final output [[1], [2, 3]].

Input: root[] = [10, 20, 30, 40, 50]
       10
      /  \
    20    30
   / \
 40   50
Output: [[10], [20, 30], [40, 50]]
Explanation: We begin with the root node 10, which forms the first level as [10]. Its children 20 and 30 make up the second level, and their children 40 and 50 form the third level, resulting in [[10], [20, 30], [40, 50]].

Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]
        1
       / \
      3   2
           \
            4
           / \
          6   5
Output: [[1], [3, 2], [4], [6, 5]]
Explanation: The traversal starts with root node 1, giving the first level [1]. At the second level, we visit its children 3 and 2 from left to right as given, then move to the third level with node 4, and finally reach the fourth level with its children 6 and 5, resulting in [[1], [3, 2], [4], [6, 5]].
"""

from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        ✅ Approach:
            - Use BFS (Breadth-First Search) to traverse the tree level by level.
            - Use a queue (deque) to keep track of nodes at the current level.
            - For each level, process all nodes currently in the queue:
              * Collect their values.
              * Add their non-null children to the queue for the next level.
            - Continue until all levels are processed.

        ⏱️ Time Complexity:
            - O(N), where N is the number of nodes in the tree.
            - Each node is visited exactly once.

        🧠 Space Complexity:
            - O(W), where W is the maximum width of the tree (max nodes at any level).
            - Queue stores at most one level of nodes.

        ! Important:
            - Uses deque for efficient O(1) pops from the left.
            - Returns a list of lists containing node values per level.
        """

        # ! Edge case: if tree is empty, return a list with an empty list
        if not root:
            return []

        ans = []                # List to store final result of level order traversal
        queue = deque([root])  # Initialize deque with root node

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.data)

                # Add children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_nodes:
                ans.append(level_nodes)

        return ans
