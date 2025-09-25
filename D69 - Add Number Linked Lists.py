"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/add-two-numbers-represented-by-linked-lists

Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
Explanation: Given numbers are 45 and 345. There sum is 390.

Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7
Output: 7 -> 0
Explanation: Given numbers are 63 and 7. There sum is 70.

Constraints:
1 <= size of both linked lists <= 106
0 <= elements of both linked lists <= 9
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, num1, num2):
        """
        ✅ Approach:
        - Reverse both input linked lists to start addition from least significant digit.
        - Traverse both lists and simulate digit-wise addition with carry handling.
        - Reuse remaining nodes if one list is longer, continuing to propagate carry.
        - Finally, reverse the result and strip leading zeroes if any.

        ⏱️ Time Complexity: O(N + M), where N and M are lengths of the two lists.
        🧠 Space Complexity: O(1), uses constant space (in-place operations).
        """

        def reverseLL(node):
            """Helper to reverse a singly linked list in-place."""
            current_node = node
            previous_node = None
            while current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            return previous_node

        # * Step 1: Reverse both input linked lists
        num1 = reverseLL(num1)
        num2 = reverseLL(num2)

        # * Step 2: Setup for result construction
        dummy = Node(-1)
        dummy_node = dummy
        carry = 0

        # * Step 3: Add corresponding digits from both lists
        while num1 and num2:
            addition = num1.data + num2.data + carry
            carry = addition // 10
            digit = addition % 10
            dummy_node.next = Node(digit)

            # Move to next nodes
            dummy_node = dummy_node.next
            num1 = num1.next
            num2 = num2.next

        # * Step 4: Process remaining nodes (if one list is longer)
        remaining = num1 if num2 is None else num2
        dummy_node.next = remaining

        # * Step 5: Propagate carry if leftover after one list ends
        while (remaining is not None) and (carry > 0):
            addition = remaining.data + carry
            remaining.data = addition % 10
            carry = addition // 10

            dummy_node = remaining
            remaining = remaining.next

        # * Step 6: Final carry (e.g., 999 + 1 => 1000)
        if carry > 0:
            dummy_node.next = Node(carry)
            dummy_node = dummy_node.next

        # * Step 7: Reverse final result to restore original digit order
        dummy = reverseLL(dummy.next)

        # * Remove any leading zeros (e.g., 000123)
        while dummy and dummy.data <= 0:
            dummy = dummy.next

        return dummy


"""
! BELOW IS INCORRECT SOLUTION BUT STILL GET PASS ON GFG
NOTE : try blow test case
    num1 = 9 -> 9 -> 9 -> 9 
    num2 = 2 -> 2
"""


class Solution:
    def addTwoLists(self, num1, num2):
        """
        ✅ Approach:
        - Reverse both linked lists to add digits from least significant (just like we do on paper).
        - Add corresponding digits node-by-node along with the carry.
        - Attach remaining part of the longer list and propagate carry if needed.
        - Finally, reverse the result list and return.

        ⏱️ Time Complexity: O(N + M) — each node visited once for reversing and addition.
        🧠 Space Complexity: O(1) — constant space (excluding output list).
        """

        def reverseLL(node):
            """Utility to reverse a linked list in-place."""
            current_node = node
            previous_node = None

            while current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            return previous_node

        # * Step 1: Reverse both input numbers to start addition from LSB
        num1 = reverseLL(num1)
        num2 = reverseLL(num2)

        dummy = Node(-1)  # Placeholder to build the result list
        dummy_node = dummy
        carry = 0

        # * Step 2: Traverse both lists and add digits with carry
        while num1 and num2:
            addition = num1.data + num2.data + carry

            carry = addition // 10
            digit = addition % 10

            dummy_node.next = Node(digit)
            dummy_node = dummy_node.next

            num1 = num1.next
            num2 = num2.next

        # * Step 3: Attach leftover nodes from longer list and add carry if any
        if num1:
            dummy_node.next = num1
            num1.data += carry
        elif num2:
            dummy_node.next = num2
            num2.data += carry
        elif carry > 0:
            dummy_node.next = Node(carry)

        # * Step 4: Reverse the result to restore original digit order
        dummy = reverseLL(dummy.next)

        # * Step 5: Remove any leading zeros (if present)
        while dummy and dummy.data <= 0:
            dummy = dummy.next

        return dummy


"""
* [Expected Approach] By storing sum on the longer list - O(m + n) Time and O(1) Space

# Python Program to add two number represented as
# linked list by storing sum on the longer list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# function to reverse the linked list
def reverse(head):
    prev = None
    curr = head

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

# function to trim leading zeros in linked list
def trimLeadingZeros(head):
    while head and head.data == 0:
        head = head.next
    return head

# Function to find the length of linked list
def countNodes(head):
    length = 0
    curr = head

    while curr is not None:
        length += 1
        curr = curr.next

    return length

# Function to add two numbers represented by linked list
def addTwoLists(num1, num2):
    num1 = trimLeadingZeros(num1)
    num2 = trimLeadingZeros(num2)
    
    # Find the length of both the linked lists
    len1 = countNodes(num1)
    len2 = countNodes(num2)
    
    # If num1 is smaller, swap the two linked lists by 
    # calling the function with reversed parameters
    if len1 < len2:
        return addTwoLists(num2, num1)

    carry = 0
    num1 = reverse(num1)
    num2 = reverse(num2)

    res = num1

    # Iterate till either num2 is not empty or carry is greater than 0
    while num2 is not None or carry != 0:
        # Add carry to num1
        num1.data += carry

        # If num2 linked list is not empty, add it to num1
        if num2 is not None:
            num1.data += num2.data
            num2 = num2.next

        # Store the carry for the next nodes
        carry = num1.data // 10

        # Store the remainder in num1
        num1.data = num1.data % 10

        # If we are at the last node of num1 but carry is
        # still left, then append a new node to num1
        if num1.next is None and carry != 0:
            num1.next = Node(0)

        num1 = num1.next

    # Reverse the resultant linked list to get 
    # the required linked list
    return reverse(res)

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    
    # Creating first linked list: 1 -> 2 -> 3
    # (represents 123)
    num1 = Node(1)
    num1.next = Node(2)
    num1.next.next = Node(3)

    # Creating second linked list: 9 -> 9 -> 9
    # (represents 999)
    num2 = Node(9)
    num2.next = Node(9)
    num2.next.next = Node(9)

    sumList = addTwoLists(num1, num2)
    printList(sumList)
"""