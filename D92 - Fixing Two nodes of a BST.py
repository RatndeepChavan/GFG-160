"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/problem/fixed-two-nodes-of-a-bst

Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original Binary search tree(BST).

Examples :
Input: root = [10, 5, 8, 2, 20]
Output: 1
Explanation: The nodes 20 and 8 were swapped. 

Input: root = [5, 10, 20, 2, 8]
Output: 1 
Explanation: The nodes 10 and 5 were swapped.

Constraints:
1 ≤ Number of nodes ≤ 103
"""
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def correctBST(self, root):
        """
        ? Corrects a Binary Search Tree (BST) where exactly two nodes have been swapped by mistake.

        ✅ Key Idea:
        - Inorder traversal of a BST should always produce a sorted (non-decreasing) sequence.
        - If two nodes are swapped, the inorder sequence will have *violations*:
            * Case 1: Two non-adjacent nodes swapped → we see **two violations**.
            * Case 2: Two adjacent nodes swapped → we see **only one violation**.
        - During inorder traversal:
            - Track `prev_node` (the last visited node).
            - If `current.data <= prev_node.data`, a violation is found.
            - On **first violation** → mark `wrong_node = prev_node`, `neighbour_node = current`.
            - On **second violation** → directly swap `wrong_node` and `current` and return.
        - If only one violation is found → the swapped nodes are adjacent.
            In that case, fix it after traversal by swapping appropriately.

        ✅ Approach:
        - Use **iterative inorder traversal with a stack** (O(H) space, O(N) time).
        - Track nodes where the sorted order breaks.
        - Perform the swap in-place.

        ⏱️ Time Complexity: O(N) (each node is visited once).
        🧠 Space Complexity: O(H) (stack for traversal, H = tree height).
        """

        wrong_node = None        # First misplaced node
        neighbor_node = None    # Node next to the wrong node (for adjacent case)
        prev_node = Node(float("-inf"))  # Initialize prev as -∞ for comparison
        stack = []
        current = root

        # Iterative inorder traversal
        while stack or current:
            # Traverse left subtree fully
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()

            # Detect violation in sorted order
            if current.data <= prev_node.data:
                if wrong_node:
                    # Second violation → swap and finish
                    wrong_node.data, current.data = current.data, wrong_node.data
                    return True
                # First violation → store candidate nodes
                wrong_node = prev_node
                neighbor_node = current

            # Update prev_node
            prev_node = current
            # Move to right subtree
            current = current.right

        # Post-traversal fix (handles adjacent swapped nodes)
        if wrong_node.data >= prev_node.data:
            # Case: wrong_node and prev_node are the swapped pair
            wrong_node.data, prev_node.data = prev_node.data, wrong_node.data
        else:
            # Case: wrong_node and neighbor_node are the swapped pair
            wrong_node.data, neighbor_node.data = neighbor_node.data, wrong_node.data

