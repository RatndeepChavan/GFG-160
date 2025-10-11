"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/construct-tree-1

Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal.

Examples:
Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
Output: [8, 7, 6, 1]

Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
Output: [3, 4, 1, 5, 2, 0]

Input: inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
Output: [2, 5, 4, 3, 1]

Constraints:
1 ≤ number of nodes ≤ 103
0 ≤ nodes -> data ≤ 103
Both the inorder and preorder arrays contain unique values.
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
        self.right = None
        self.left = None


class Solution:
    def buildTree(self, inorder, preorder):
        """
        ? Reconstructs a binary tree from its inorder and preorder traversals.

        Args:
            inorder (list[int]): A list representing the inorder traversal of the tree.
            preorder (list[int]): A list representing the preorder traversal of the tree.

        Returns:
            Node: The root node of the reconstructed binary tree.

        ✅ Approach (Recursive):
            - **Base case:** If either `inorder` or `preorder` list is empty, it signifies an empty subtree, so we return `None`.
            - **Identify the root:** In a preorder traversal, the first element is always the root of the tree.
            - **Create the root node:** Create a new `Node` with this value.
            - **Find the split point:** Locate the root's value in the `inorder` traversal. This index (`mid`) divides the `inorder` list into the left and right subtrees.
            - **Recursive calls:**
                - The left subtree's inorder traversal is `inorder[:mid]`. Its preorder traversal is `preorder[1:mid+1]`. Recursively build the left child.
                - The right subtree's inorder traversal is `inorder[mid+1:]`. Its preorder traversal is `preorder[mid+1:]`. Recursively build the right child.
            - **Return the root:** Return the newly created `node`.

        ⏱️ Time Complexity:
            - **O(N^2)**, where N is the number of nodes.
            - The `list.index()` call takes O(N) time in each recursive step. Slicing lists also contributes to this complexity.
            - In the worst case (a skewed tree), this leads to a total time complexity of O(N^2).

        🧠 Space Complexity:
            - **O(H)** for the recursion stack, where H is the height of the tree.
            - In the worst case (a skewed tree), this is **O(N)**.
        """
        if not inorder or not preorder:
            # Base case: if either list is empty, return None
            return None

        # The first element of preorder is the root
        node_data = preorder[0]
        node = Node(node_data)
        
        # Find the root's position in inorder to split the list for left and right subtrees
        mid = inorder.index(node_data)
        
        # Recursively build the left and right subtrees
        # Left subtree: inorder is `inorder[:mid]`, preorder is `preorder[1: mid+1]`
        node.left = self.buildTree(inorder[:mid], preorder[1 : mid + 1])
        # Right subtree: inorder is `inorder[mid+1:]`, preorder is `preorder[mid+1:]`
        node.right = self.buildTree(inorder[mid + 1:], preorder[mid + 1:])
        
        return node


# ----------------------------------------------------------------------------------------------------------------------


class Solution_Optimized:
    def buildTree(self, inorder, preorder):
        """
        ? An optimized recursive solution to reconstruct a binary tree from its traversals.

        This approach uses a hash map to quickly find the index of elements in the inorder traversal,
        reducing the time complexity of the `list.index()` call.

        Args:
            inorder (list[int]): The inorder traversal.
            preorder (list[int]): The preorder traversal.

        Returns:
            Node: The root of the reconstructed tree.

        ✅ Approach:
            - Create a dictionary `inorder_map` to store `value: index` pairs for the `inorder` list.
            - Use a helper function that takes the boundaries of the sub-arrays as parameters (e.g., `pre_start`, `in_start`, `in_end`).
            - The root is still `preorder[pre_start]`.
            - Use the `inorder_map` to find the root's index (`in_root_idx`) in O(1) time.
            - Calculate the size of the left subtree (`left_size`).
            - Recursively build the left and right subtrees by adjusting the boundaries.
            - `left` subtree: `_build_helper(pre_start + 1, in_start, in_root_idx - 1)`
            - `right` subtree: `_build_helper(pre_start + left_size + 1, in_root_idx + 1, in_end)`

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes.
            - The hash map allows for O(1) lookups. Each node is processed exactly once.

        🧠 Space Complexity:
            - **O(N)** for the `inorder_map` and the recursion stack.
            - The `inorder_map` stores all N nodes. The recursion stack can be up to O(N) for a skewed tree.
        """
        # Create a hash map for O(1) lookups of element indices in the inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # We need an index to keep track of the current root in the preorder traversal
        self.preorder_index = 0
        
        def _build_helper(in_start, in_end):
            # Base case: if the inorder segment is invalid
            if in_start > in_end:
                return None
            
            # The current root is taken from the preorder traversal
            root_val = preorder[self.preorder_index]
            node = Node(root_val)
            self.preorder_index += 1
            
            # Find the index of the root in the inorder traversal
            in_root_idx = inorder_map[root_val]
            
            # Recursively build the left and right subtrees
            node.left = _build_helper(in_start, in_root_idx - 1)
            node.right = _build_helper(in_root_idx + 1, in_end)
            
            return node
            
        return _build_helper(0, len(inorder) - 1)

# ----------------------------------------------------------------------------------------------------------------------


class Solution_Iterative:
    def buildTree(self, inorder, preorder):
        """
        ? Iterative solution to reconstruct a binary tree from its traversals.

        This approach uses a stack to build the tree. It processes the preorder and inorder lists
        simultaneously to determine parent-child relationships.

        Args:
            inorder (list[int]): The inorder traversal.
            preorder (list[int]): The preorder traversal.

        Returns:
            Node: The root of the reconstructed tree.

        ✅ Approach:
            - If `preorder` is empty, return `None`.
            - Create the root node from `preorder[0]` and push it onto a stack.
            - Iterate through `preorder` from the second element.
            - For each element, check if it's the child of the top of the stack by comparing it with the current element of `inorder`.
            - If it's the right child, pop from the stack until the current node's value is found. The last popped node will be the parent of the new node.
            - Push the new node onto the stack.

        ⏱️ Time Complexity:
            - **O(N)**, where N is the number of nodes.
            - We iterate through the `preorder` list once, and each node is pushed and popped from the stack at most once.

        🧠 Space Complexity:
            - **O(H)** for the stack, where H is the height of the tree.
            - In the worst case (a skewed tree), this is **O(N)**.
        """
        if not preorder:
            return None

        # Initialize the stack and the inorder pointer
        root = Node(preorder[0])
        stack = [root]
        inorder_idx = 0

        for i in range(1, len(preorder)):
            current_node = Node(preorder[i])
            last_node = stack[-1]

            # If the last node on the stack is not the current element in inorder,
            # it means the current node is its left child.
            if last_node.data != inorder[inorder_idx]:
                last_node.left = current_node
            else:
                # Pop nodes from the stack until we find the parent of the current node.
                # This parent will be the last node popped from the stack before the inorder index matches.
                while stack and stack[-1].data == inorder[inorder_idx]:
                    last_node = stack.pop()
                    inorder_idx += 1
                
                # The current node is the right child of the last node popped.
                last_node.right = current_node
            
            # Push the new node onto the stack
            stack.append(current_node)
            
        return root