"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/rotate-a-linked-list

Given the head of a singly linked list, your task is to left rotate the linked list k times.

Examples:

Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
Output: 50 -> 10 -> 20 -> 30 -> 40
Explanation:
Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
Rotate 4: 50 -> 10 -> 20 -> 30 -> 40

Input: head = 10 -> 20 -> 30 -> 40 , k = 6
Output: 30 -> 40 -> 10 -> 20

Constraints:
1 <= number of nodes <= 105
0 <= k <= 109
0 <= data of node <= 109
"""


class Solution:
    def rotate(self, head, k):
        """
        ✅ Approach:
            1. Compute the length of the linked list.
            2. Normalize k (k = k % length) to handle cases where k > length.
            3. If k == 0, no rotation is needed.
            4. Traverse to the (k-1)th node — this will be the new tail.
            5. Set the (k)th node as the new head.
            6. Break the list at (k-1)th node (tail.next = None).
            7. Connect the original tail to the original head.
            8. Return the new head.

        ⏱️ Time Complexity: O(N)
            - One traversal to get the length
            - One traversal to reach (k-1)th node

        🧠 Space Complexity: O(1)
            - No extra space used, only pointer manipulation

        Args:
            head (Node): Head of the singly linked list
            k (int): Number of positions to rotate left

        Returns:
            Node: New head of the rotated linked list
        """
        # ! Edge Case : Empty list, One node or k == 0
        if not head or not head.next or k == 0:
            return head

        # * Step 1: Get the length and tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # * Step 2: Normalize k
        k = k % length

        # ! Edge case : k % length == 0 → no rotation needed
        if k == 0:
            return head

        # * Step 3: Reach the (k-1)th node
        current = head
        for _ in range(k - 1):
            current = current.next

        # * Step 4: Rewire pointers
        new_head = current.next
        current.next = None
        tail.next = head

        return new_head
