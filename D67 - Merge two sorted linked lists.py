"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/merge-two-sorted-linked-lists

Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

Examples:

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4

Constraints:
1 <= no. of nodes<= 103
0 <= node->data <= 105
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self, head1, head2):
        """
        Merges two sorted singly linked lists into one sorted linked list.
        This does not create new nodes; it reuses existing ones by adjusting pointers.

        ✅ Approach:
        - Use a dummy node to simplify edge cases.
        - Use a `tail` pointer to build the merged list.
        - Walk through both lists, always attaching the smaller node.
        - Attach remaining nodes from the list that is not yet exhausted.

        ⏱️ Time Complexity: O(N + M)
        🧠 Space Complexity: O(1) — no new nodes created
        """
        dummy = Node(-1)  # Temporary dummy node to start the merged list
        tail = dummy  # Tail pointer to track the last node of merged list

        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next  # Move tail forward

        # Attach remaining part
        tail.next = head1 if head1 else head2

        return dummy.next  # Return the real head (skipping dummy)
