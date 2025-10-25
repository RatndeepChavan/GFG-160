"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/heap-gfg-160/problem/merge-k-sorted-linked-lists

Given an array arr[] of n sorted linked lists of different sizes. Your task is to merge all these lists into a single sorted linked list and return the head of the merged list.

Constraints
1 ≤ total no. of nodes ≤ 105
1 ≤ node->data ≤ 103
"""

# Definition for Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# ------------------------------------------------------------------
# * 🟢 1. Array + Sorting
# ------------------------------------------------------------------
class SolutionArraySort:
    """
    🧩 Approach:
    ------------
    - Traverse all k linked lists.
    - Collect all nodes into an array.
    - Sort the array by node value.
    - Reconnect nodes to form a sorted linked list.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N log N)**   (N = total number of nodes across all lists)
    - 🧠 **Space: O(N)** extra (array of nodes)

    NOTE: Simple but not optimal — uses extra memory for storing all nodes.
    """

    def mergeKLists(self, arr):
        if not arr:
            return None

        # * STEP1 : Collect all nodes into an array
        elements = []
        for head in arr:
            current = head
            while current:
                elements.append(current)
                current = current.next

        # * STEP2 : Sort nodes by value
        elements.sort(key=lambda node: node.data)

        # * STEP3 :Reconnect nodes
        for i in range(len(elements) - 1):
            elements[i].next = elements[i + 1]

        return None


# ------------------------------------------------------------------
# * 🟡 2. Min-Heap
# ------------------------------------------------------------------
import heapq

class SolutionHeap:
    """
    🧩 Approach:
    ------------
    - Use a Min-Heap to always extract the smallest node among k heads.
    - Push the next node from the extracted list into the heap.
    - Continue until heap is empty.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N log k)** (heap operations log k, N = total nodes)
    - 🧠 **Space: O(k)** for heap

    ✅ Much better than array+sort when k is small relative to N.
    """

    def mergeKLists(self, arr):
        # ! Edge case : empty array
        if not arr:
            return None

        heap = []
        
        # * STEP! : Push first node of each list into heap
        for i, head in enumerate(arr):
            if head:
                heapq.heappush(heap, (head.data, i, head))  # (value, list_index, node)
                
                # ? Why do we store (value, index, node) instead of just (value, node)?
                # when two elements with the same value go into the heap, the heap will try to compare the second item
                # Suppose we push (5, NodeA) and (5, NodeB). Python first checks 5 == 5, then tries to compare NodeA with NodeB. → TypeError.

        dummy = Node(-1)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.data, i, node.next))

        return dummy.next


# ------------------------------------------------------------------
# * 🔴 3. Divide & Conquer (Pairwise Merge)
# ------------------------------------------------------------------
class SolutionDivideConquer:
    """
    🧩 Approach:
    ------------
    - Repeatedly merge lists in pairs (like merge sort).
    - Each pass halves the number of lists.
    - Continue until one sorted list remains.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N log k)** (N = total nodes, k = number of lists)
    - 🧠 **Space: O(k)**  extra (iterative merging, no heap/array needed)

    ✅ Optimal for large k.
    """

    def mergeKLists(self, arr):
        # ! Edge case : empty array
        if not arr:
            return None
        
        # * Keep merging until only one list remains
        while len(arr) > 1:
            merged = []
            # Merge two list at a time
            for i in range(0, len(arr), 2):
                l1 = arr[i]
                l2 = arr[i + 1] if i + 1 < len(arr) else None
                merged.append(self.mergeTwoLists(l1, l2))
            arr = merged

        return arr[0]

    def mergeTwoLists(self, l1, l2):
        """Merge two sorted linked lists into one sorted list."""
        dummy = Node(0)
        curr = dummy

        while l1 and l2:
            if l1.data < l2.data:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next
