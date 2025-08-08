"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/reverse-a-linked-list

Given the head of a linked list, the task is to reverse this list and return the reversed head.

Examples:

Input: head: 1 -> 2 -> 3 -> 4 -> NULL
Output: head: 4 -> 3 -> 2 -> 1 -> NULL
Explanation:

Input: head: 2 -> 7 -> 10 -> 9 -> 8 -> NULL
Output: head: 8 -> 9 -> 10 -> 7 -> 2 -> NULL
Explanation:

Input: head: 2 -> NULL
Output: 2 -> NULL
Explanation:

Constraints:
1 <= number of nodes, data of nodes <= 105
"""


# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        ✅ Approach:
            - Iterate through the list.
            - At each node, reverse the pointer direction (`current.next = prev`).
            - Keep track of previous and next nodes to avoid breaking links.

        ⏱️ Time Complexity: O(n)
            - Each node is visited once.

        🧠 Space Complexity: O(1)
            - In-place reversal using pointer manipulation.

        ! Edge Case:
            - Empty list (head = None) → return None
            - Single node → returns same node

        Args:
            head (Node): Head of the singly linked list

        Returns:
            Node: New head of the reversed linked list
        """
        # ✅ Start with None since new tail should point to None
        prev_node = None

        while head is not None:
            next_node = head.next  # ? Temporarily store the next node
            head.next = prev_node  # ? Reverse the link
            prev_node = head  # Move prev_node forward
            head = next_node  # Move head forward

        return prev_node  # ✅ This is the new head after full reversal
