"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/remove-loop-in-linked-list

Given the head of a singly linked list, the task is to remove a cycle if present. A cycle exists when a node's next pointer points back to a previous node, forming a loop. Internally, a variable pos denotes the index of the node where the cycle starts, but it is not passed as a parameter. The terminal will print true if a cycle is removed otherwise, it will print false.

Constraints:
1 ≤ size of linked list ≤ 105
"""


class Solution:
    def removeLoop(self, head):
        """
        ✅ Approach in Plain English:

        1. First, detect if a cycle exists using Floyd's Cycle Detection Algorithm
            (i.e., slow and fast pointers).

        2. If no loop is found, return immediately.

        3. If a loop exists:
            - Reset the slow pointer to head
            - Instead of finding the loop's *start node*, we cleverly use:
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next

            - Once both slow.next and fast.next point to the *same node*,
                that node is the start of the loop.

            - We then break the loop by setting:
                fast.next = None

        ❗ Why not find the loop's start explicitly?

            Normally, people find the start of the loop first, then iterate
            again from there to locate the node just before the start (to cut it).
            But that needs *two* traversals.

            Instead, by comparing `slow.next == fast.next`, we eliminate the need
            to find the loop's start separately and directly find the node just
            before the loop starts — allowing us to break it efficiently.

        ⏱️ Time: O(n)
        🧠 Space: O(1)
        """

        slow = fast = head

        # * Step 1: Detect loop using Floyd’s cycle detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return  # No loop

        # * Step 2: Find the start of the loop
        slow = head
        if slow == fast:
            # ! Special case: loop starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # * Step 3: Break the loop
        fast.next = None  # ✅ Loop removed
