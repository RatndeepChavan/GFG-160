"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/boundary-traversal-of-binary-tree

Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
Output: [1, 2, 4, 8, 9, 6, 7, 3]

Input: root[] = [1, N, 2, N, 3, N, 4, N, N] 
Output: [1, 4, 3, 2]
Explanation:
Left boundary: [1] (as there is no left subtree)
Leaf nodes: [4]
Right boundary: [3, 2] (in reverse order)
Final traversal: [1, 4, 3, 2]

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
    def get_leaf(self, node):
        """
        ? Recursively finds all leaf nodes of a subtree.

        Args:
            node (Node): The current node in the binary tree.

        Returns:
            list[int]: A list containing the data of all leaf nodes in the subtree.
            
        ✅ Approach (Recursive):
            - **Base case:** If the node is `None`, return an empty list.
            - **Leaf check:** If the node has no children (`node.left` is `None` AND `node.right` is `None`), it's a leaf. Return a list containing its data.
            - **Recursive step:** Recursively call `get_leaf` on the left and right children and combine the results.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes in the subtree. Each node is visited once.

        🧠 Space Complexity:
            - **O(H)** for the recursion stack, where H is the height of the tree.
            - In the worst case (a skewed tree), this is **O(N)**.
        """
        if not node:
            return []
        
        if not node.left and not node.right:
            return [node.data]
            
        left_leaves = self.get_leaf(node.left)
        right_leaves = self.get_leaf(node.right)
        
        return left_leaves + right_leaves

    def boundaryTraversal(self, root):
        """
        ? Performs a boundary traversal of a binary tree.

        The traversal proceeds in a clockwise manner, consisting of:
        1. The root node.
        2. The left boundary nodes (top-to-bottom).
        3. The leaf nodes (left-to-right).
        4. The right boundary nodes (bottom-to-top).

        Args:
            root (Node): The root of the binary tree.

        Returns:
            list[int]: A list containing the nodes' data in boundary traversal order.

        ✅ Approach:
            - A **list** is used to store the boundary elements in order.
            - Each step of the traversal is handled separately.
            - The `get_leaf` helper function is used to find all leaf nodes.
            
        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes, as we visit each node on the boundary and all leaf nodes once.

        🧠 Space Complexity:
            - **O(H)**, for the recursion stack and temporary lists, where H is the height of the tree.
        """
        # ! Edge Case: An empty tree has no boundary.
        if not root:
            return []

        boundary_elements = [root.data]
        
        # * Step 1: Traverse the left boundary.
        node = root.left
        while node:
            # We add a node to the boundary list only if it's not a leaf.
            if node.left or node.right:
                boundary_elements.append(node.data)
                
            # Prefer going to the left child; if none exists, go right.
            node = node.left if node.left  else node.right

        # * Step 2: Traverse all the leaf nodes from left to right.
        boundary_elements += self.get_leaf(root.left)
        boundary_elements += self.get_leaf(root.right)
        
        # * Step 3: Traverse the right boundary.
        # ? We need a separate list to store the nodes as we traverse top-down.
        right_boundary = []
        node = root.right
        while node:
            # We add a node to the right boundary list only if it's not a leaf.
            if node.left or node.right:
                right_boundary.append(node.data)
            
            # Prefer going to the right child; if none exists, go left.
            node = node.right if node.right else node.left
        
        # Reverse the list to get the bottom-up order and append it to the result.
        boundary_elements += reversed(right_boundary)
        
        return boundary_elements


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
    def get_left_boundary(self, node):
        """
        🌿 Collects the **left boundary nodes** of the binary tree (excluding leaf nodes).

        Args:
            node (Node): The left child of the root.

        Returns:
            list[int]: A list containing the left boundary nodes in **top-to-bottom** order.

        ✅ Approach (Iterative):
            - Traverse down the left side of the tree.
            - At each step:
                - Add the current node **only if it's not a leaf**.
                - Prefer going left; if no left child, go right.

        ⏱️ Time Complexity:
            - **O(H)**, where H is the height of the tree.
            - Each boundary node is visited once.

        🧠 Space Complexity:
            - **O(1)**, since no recursion is used; only a list for results.
        """
        boundary = []
        while node:
            if node.left or node.right:  # skip leaves
                boundary.append(node.data)
            node = node.left if node.left else node.right
        return boundary

    def get_right_boundary(self, node):
        """
        🌴 Collects the **right boundary nodes** of the binary tree (excluding leaf nodes).

        Args:
            node (Node): The right child of the root.

        Returns:
            list[int]: A list containing the right boundary nodes in **bottom-to-top** order.

        ✅ Approach (Iterative):
            - Traverse down the right side of the tree.
            - At each step:
                - Add the current node **only if it's not a leaf**.
                - Prefer going right; if no right child, go left.
            - Reverse the collected nodes to maintain bottom-to-top order.

        ⏱️ Time Complexity:
            - **O(H)**, where H is the height of the tree.
            - Each boundary node is visited once.

        🧠 Space Complexity:
            - **O(1)**, ignoring output list.
        """
        boundary = []
        while node:
            if node.left or node.right:  # skip leaves
                boundary.append(node.data)
            node = node.right if node.right else node.left
        return boundary[::-1]  # reverse for bottom-to-top

    def get_leaf(self, node):
        """
        🍂 Collects all **leaf nodes** in the subtree rooted at `node`.

        Args:
            node (Node): The current node in the binary tree.

        Returns:
            list[int]: A list containing all leaf node values in **left-to-right** order.

        ✅ Approach (Recursive):
            - **Base case:** If node is `None`, return empty list.
            - **Leaf check:** If node has no children, return its value.
            - **Recursive step:** Collect leaves from left and right subtrees and merge.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes in the subtree.
            - Each node is visited once.

        🧠 Space Complexity:
            - **O(H)** for recursion stack, where H is tree height.
            - Worst case (skewed tree): **O(N)**.
        """
        if not node:
            return []
        if not node.left and not node.right:
            return [node.data]
        return self.get_leaf(node.left) + self.get_leaf(node.right)

    def boundaryTraversal(self, root):
        """
        🌐 Performs the **boundary traversal** of a binary tree.

        Traversal order:
        1️⃣ Root node  
        2️⃣ Left boundary nodes (excluding leaves)  
        3️⃣ Leaf nodes (from left to right)  
        4️⃣ Right boundary nodes (excluding leaves, in bottom-to-top order)  

        Args:
            root (Node): The root of the binary tree.

        Returns:
            list[int]: A list containing the nodes' data in **boundary traversal order**.

        ✅ Approach:
            - Handle the **edge case**: If the tree is empty, return [].
            - Start with the root node.
            - Add left boundary nodes using `get_left_boundary`.
            - Add all leaf nodes using `get_leaf`.
            - Add right boundary nodes using `get_right_boundary`.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the total number of nodes.
            - Each node is visited at most once.

        🧠 Space Complexity:
            - **O(H)** for recursion stack in `get_leaf`.
            - Iterative traversals (`get_left_boundary` & `get_right_boundary`) use **O(1)** extra space.
        """
        if not root:
            return []

        result = [root.data]  # Step 1: root

        # Step 2: left boundary
        result += self.get_left_boundary(root.left)

        # Step 3: leaf nodes
        result += self.get_leaf(root.left)
        result += self.get_leaf(root.right)

        # Step 4: right boundary
        result += self.get_right_boundary(root.right)

        return result
