"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/reverse-a-linked-list-in-groups-of-given-size

Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

Examples:

Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5
Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.

Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output: 3 -> 2 -> 1 -> 5 -> 4
Explanation: The first 3 elements 1, 2, 3 are reversed first and then left out elements 4, 5 are reversed. Hence, the resultant linked list is 3 -> 2 -> 1 -> 5 -> 4.

Constraints:
1 <= size of linked list <= 105
1 <= data of nodes <= 106
1 <= k <= size of linked list
"""


class Solution:
    def reverseKGroup(self, head, k):
        """
        ✅ Approach:
        - Traverse the list group by group.
        - Reverse each group *in-place* while counting `k` nodes.
        - Use pointers to reconnect the reversed groups properly.
        - No pre-check for group size; even the last group is reversed.

        ⏱️ Time Complexity: O(N), where N is number of nodes (each visited once).
        🧠 Space Complexity: O(1), in-place pointer manipulation.
        """

        # ! Edge case: if list is empty or has only one node, return as-is
        if not head or not head.next or k <= 1:
            return head

        # `previous_start` tracks the tail of the previously reversed group
        previous_start = None

        # `current_start` is the starting node of the group to be reversed
        current_start = head

        # `new_head` will be updated once with the head of the first reversed group
        new_head = None

        while current_start:
            # * Step 1: Reverse k nodes starting from `current_start`
            current_node = current_start
            previous_node = None
            length = 0

            while length < k and current_node:
                next_node = current_node.next
                current_node.next = previous_node

                previous_node = current_node
                current_node = next_node

                length += 1

            # * Step 2: Connect reversed part to the rest of the list
            if new_head is None:
                # First group reversed
                # ? so new head will be tail of first group before reversing
                new_head = previous_node
            else:
                # Connect previously reversed group tail to current reversed group head
                previous_start.next = previous_node

            # * Step 3: Prepare for the next group
            previous_start = current_start
            current_start = current_node

            """
            # ? previous_start vs current_start
            We are reversing at distance k. 
            So previous group head connects to current tail. (as per input)
            e.g. 
                1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 , k = 3
                if divide at 3 we get (1 2 3) and (4 5 6), so heads (1, 4), tails(3, 6)
                if we reverse it then (3 2 1) and (6 5 4)
                after connect (3 2 1 -> 6 5 4) if we compare it with i/p we can see:
                    - head of first group get connect to tail of current group
                    - So if we save that starting head while traversing so can simply connect it.
                    - So as per input variable name is previous_start (use to store previous head)
                    - But after connecting we know similarly we need current group head when we reach next group tail. So we update it with current start.
                NOTE : In above discussion we are considering head and tail as per input dividing in k length group
            """

        # Return the new head after all groups are reversed
        return new_head
