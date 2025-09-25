"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/clone-a-linked-list-with-next-and-random-pointer

You are given a special linked list with n nodes where each node has two pointers a next pointer that points to the next node of the singly linked list, and a random pointer that points to the random node of the linked list.

Construct a copy of this linked list. The copy should consist of the same number of new nodes, where each new node has the value corresponding to its original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list, such that it also represent the same list state. None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

NOTE : Original linked list should remain unchanged.

Examples:

Input: head = [[1, 3], [3, 3], [5, NULL], [9, 3]]
Output: head = [[1, 3], [3, 3], [5, NULL], [9, 3]]
Explanation:
Node 1 points to Node 2 as its NEXT and Node 3 as its RANDOM.
Node 2 points to Node 3 as its NEXT and Node 3 as its RANDOM.
Node 3 points to Node 4 as its NEXT and NULL as its RANDOM.
Node 4 points to NULL as its NEXT and Node 3 as its RANDOM.

Input: head = [[1, 3], [2, 1], [3, 5], [4, 3], [5, 2]]
Output: head = [[1, 3], [2, 1], [3, 5], [4, 3], [5, 2]]
Explanation:
Node 1 points to Node 2 as its NEXT and Node 3 as its RANDOM.
Node 2 points to Node 3 as its NEXT and Node 1 as its RANDOM.
Node 3 points to Node 4 as its NEXT and Node 5 as its RANDOM.
Node 4 points to Node 5 as its NEXT and Node 3 as its RANDOM.
Node 5 points to NULL as its NEXT and Node 2 as its RANDOM.

Input: head = [[7, NULL], [7, NULL]]
Output: head = [[7, NULL], [7, NULL]]
Explanation:
Node 1 points to Node 2 as its NEXT and NULL as its RANDOM.
Node 2 points to NULL as its NEXT and NULL as its RANDOM.

Constraints:
1 <= n <= 100
0 <= node->data <= 1000
"""


class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        # * Step 1: Interleave copy nodes between original nodes
        current_node = head
        while current_node:
            copy_node = Node(current_node.data)
            copy_node.next = current_node.next
            current_node.next = copy_node
            current_node = copy_node.next

        # * Step 2: Set random pointers for the copied nodes
        current_node = head
        while current_node:
            copy_node = current_node.next
            if current_node.random:
                copy_node.random = current_node.random.next
            current_node = copy_node.next

        # * Step 3: Restore original list and extract copy
        current_node = head
        new_head = head.next
        while current_node:
            copy_node = current_node.next
            current_node.next = copy_node.next  # Restore original

            if copy_node.next:  # Set next for cloned list
                copy_node.next = copy_node.next.next

            current_node = current_node.next

        return new_head
