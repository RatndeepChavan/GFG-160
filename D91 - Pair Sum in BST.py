"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/find-a-pair-with-given-target-in-bst

Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing up to the target. 

Examples:
Input: root = [7, 3, 8, 2, 4, N, 9], target = 12
Output: True
Explanation: In the binary tree above, there are two nodes (8 and 4) that add up to 12.

Input: root = [9, 5, 10, 2, 6, N, 12], target = 23
Output: False
Explanation: In the binary tree above, there are no such two nodes exists that add up to 23.

Constraints:
1 ≤ Number of Nodes ≤ 105
1 ≤ target ≤ 106
"""

# ----------------------------------------------------------------------------------------------------------------------
# * Tree Node
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
# * Solution 1: BFS + Hash Set
# ----------------------------------------------------------------------------------------------------------------------

class Solution_BFS:
    def findTarget(self, root, target):
        """
        ? Determines if there exist two distinct nodes in the BST whose values sum up to `target`.

        ✅ Approach (BFS + Hash Set):
            - Traverse the tree level by level (BFS).
            - Keep a set (`element_tracker`) of visited node values.
            - For each node:
                - Compute the `require_element = target - current.data`.
                - If `require_element` already exists in the set → return True.
                - Otherwise, add `current.data` to the set.
            - Continue BFS until all nodes are processed.

        ⏱️ Time Complexity:
            - **O(N)**, since each node is visited once.

        🧠 Space Complexity:
            - **O(N)** for the hash set and BFS queue.
        """
        if not root:
            return False

        element_tracker = set()
        queue = [root]

        while queue:
            current = queue.pop(0)  # O(N) if plain list; better: collections.deque
            require_element = target - current.data

            if require_element in element_tracker:
                return True

            element_tracker.add(current.data)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return False


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 2: DFS + Hash Set (Recursive)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_DFS:
    def findTarget(self, root, target):
        """
        ? Determines if two nodes in the BST sum to `target` using DFS + hash set.

        ✅ Approach:
            - Use a recursive DFS traversal.
            - Keep a set of seen values.
            - For each node, check if `target - node.data` exists in the set.
            - If yes → return True.
            - Else add the node’s value and continue recursion.

        ⏱️ Time Complexity: O(N)
        🧠 Space Complexity: O(N)
        """
        seen = set()

        def dfs(node):
            if not node:
                return False
            if (target - node.data) in seen:
                return True
            seen.add(node.data)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 3: Two-Pointer Inorder Traversal (Optimized for BST)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_TwoPointer:
    def findTarget(self, root, target):
        """
        ? Determines if two nodes sum to `target` using BST property + two-pointer technique.

        ✅ Approach:
            - Perform an inorder traversal → gives sorted array of node values.
            - Apply the classic two-pointer technique:
                - Start with `i = 0`, `j = len(arr) - 1`.
                - If arr[i] + arr[j] == target → return True.
                - If sum < target → move i++.
                - If sum > target → move j--.
            - Return False if no pair found.

        ⏱️ Time Complexity: O(N)
        🧠 Space Complexity: O(N) (array of inorder traversal)
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)

        arr = inorder(root)
        i, j = 0, len(arr) - 1

        while i < j:
            total = arr[i] + arr[j]
            if total == target:
                return True
            elif total < target:
                i += 1
            else:
                j -= 1
        return False


# ----------------------------------------------------------------------------------------------------------------------
# * Solution 4: Morris Traversal + Two Iterators (O(1) space)
# ----------------------------------------------------------------------------------------------------------------------

class Solution_Morris:
    def findTarget(self, root, target):
        """
        ✅ Approach (Morris Traversal with Two Iterators):
            - Morris traversal generates inorder sequence without recursion/stack (O(1) space).
            - Use two Morris-based iterators:
                * `next_smallest()` → gives next element in ascending order.
                * `next_largest()` → gives next element in descending order.
            - Move the two iterators like two pointers until they meet.

        ⏱️ Time: O(N)
        🧠 Space: O(1)
        """
        if not root:
            return False

        # Helper: inorder generator (Morris)
        def inorder_gen(node):
            current = node
            while current:
                if not current.left:
                    yield current.data
                    current = current.right
                else:
                    pred = current.left
                    while pred.right and pred.right is not current:
                        pred = pred.right
                    if not pred.right:
                        pred.right = current
                        current = current.left
                    else:
                        pred.right = None
                        yield current.data
                        current = current.right

        # Helper: reverse inorder generator (Morris)
        def rev_inorder_gen(node):
            current = node
            while current:
                if not current.right:
                    yield current.data
                    current = current.left
                else:
                    succ = current.right
                    while succ.left and succ.left is not current:
                        succ = succ.left
                    if not succ.left:
                        succ.left = current
                        current = current.right
                    else:
                        succ.left = None
                        yield current.data
                        current = current.left

        # Initialize two generators
        left_gen = inorder_gen(root)
        right_gen = rev_inorder_gen(root)

        left_val = next(left_gen, None)
        right_val = next(right_gen, None)

        while left_val is not None and right_val is not None and left_val < right_val:
            total = left_val + right_val
            if total == target:
                return True
            elif total < target:
                left_val = next(left_gen, None)
            else:
                right_val = next(right_gen, None)

        return False