"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/find-the-first-node-of-loop-in-linked-list--170645


Given a head of the singly linked list. If a loop is present in the list then return the first node of the loop else return NULL.

Constraints:
1 <= no. of nodes <= 106
1 <= node->data <= 106
"""


class Solution:
    def findFirstNode(self, head):
        """
        ✅ Approach: Floyd's Tortoise & Hare + Loop Start Finder

        1. Detect if loop exists using fast and slow pointers.
        2. If they meet, reset one pointer to head and move both step-by-step.
        3. Their meeting point is the start of the loop.

        ⏱️ Time: O(n)
        🧠 Space: O(1)
        """
        slow = fast = head

        # Step 1: Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None  # 🚫 No loop

        # Step 2: Find start of loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # ✅ This is the start of the loop
