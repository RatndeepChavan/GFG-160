"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/detect-loop-in-linked-list

You are given the head of a singly linked list. Your task is to determine if the linked list contains a loop. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

Custom Input format:
A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

Examples:

Input: head: 1 -> 3 -> 4, pos = 2
Output: true
Explanation: There exists a loop as last node is connected back to the second node.

Input: head: 1 -> 8 -> 3 -> 4, pos = 0
Output: false
Explanation: There exists no loop in given linked list.

Input: head: 1 -> 2 -> 3 -> 4, pos = 1
Output: true
Explanation: There exists a loop as last node is connected back to the first node.


Constraints:
1 ≤ number of nodes ≤ 104
1 ≤ node->data ≤ 103
0 ≤ pos ≤ Number of nodes in Linked List
"""


class Solution:
    def detectLoop(self, head):
        """
        ✅ Approach: Floyd's Cycle Detection (Tortoise and Hare)

        We move two pointers at different speeds:
        - slow_ptr moves one step at a time
        - fast_ptr moves two steps at a time

        If there's a loop, they will eventually meet.

        ⏱️ Time: O(n)
        🧠 Space: O(1)
        """
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True  # ✅ Loop found!

        return False  # 🚫 No loop found
