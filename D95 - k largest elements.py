"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/heap-gfg-160/problem/k-largest-elements4206

Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order.

Examples:
Input: arr[] = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]
Explanation: 1st largest element in the array is 787 and second largest is 23.

Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]
Explanation: Three Largest elements in the array are 50, 30 and 23.

Input: arr[] = [12, 23], k = 1
Output: [23]
Explanation: 1st Largest element in the array is 23.

Constraints:
1 ≤ k ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
"""

import heapq


# -------------------------------
# 1. Using Python's heapq library
# -------------------------------
def k_largest(nums, k):
    """
    Return k largest elements in descending order using heapq (min-heap).


    Approach:
    ---------
    - Build a min-heap of size k.
    - Traverse the rest of the array:
        - If the current element is larger than the smallest in the heap (root),
        replace it (so heap always stores k largest so far).
    - At the end, the heap contains k largest elements in arbitrary order.
    - Sort them in descending order for the final result.

    Complexity:
    -----------
    - Heap build: O(k)
    - Remaining elements: O((n-k) * log k)
    - Sorting final k elements: O(k log k)
    - Overall: O(n log k)
    - Space: O(k)

    Parameters:
        nums (list[int]): Input array
        k (int): Number of largest elements to extract

    Returns:
        list[int]: k largest elements sorted in descending order
    """
    # 1. Build min-heap of first k elements → O(k)
    heap = nums[:k]
    heapq.heapify(heap)  # transforms list into a heap

    # 2. Process the remaining elements → O((n-k) log k)
    for num in nums[k:]:
        if num > heap[0]:  # compare with smallest in heap
            heapq.heapreplace(heap, num)  # pop + push in O(log k)

    # 3. Heap now contains k largest elements (unordered)
    # Sort them in descending order
    return sorted(heap, reverse=True)


# -------------------------------------
# 2. Custom MinHeap implementation
# -------------------------------------
class MinHeap:
    """Custom MinHeap class to replicate heapq functionality."""

    def __init__(self):
        self.heap = []

    def push(self, val):
        """Insert new value into heap."""
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the smallest element (root) from heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move last element to root and bubble down
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def replace(self, val):
        """
        Replace root with new value (used in k largest problem).
        Assumes val > root, ensuring heap still tracks k largest.
        """
        root = self.heap[0]
        self.heap[0] = val
        self._bubble_down(0)
        return root

    def peek(self):
        """Return smallest element (root) without removing it."""
        return self.heap[0] if self.heap else None

    def _bubble_up(self, index):
        """Maintain heap property upwards from index."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Swap child and parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index, parent = parent, (parent - 1) // 2

    def _bubble_down(self, index):
        """Maintain heap property downwards from index."""
        n = len(self.heap)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index

            # Check left child: if it exists and is smaller → update smallest
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Check right child: if it exists and is smaller than current smallest
            # (which might be the parent or the left child) → update smallest
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break


def k_largest_custom(nums, k):
    """
    Return k largest elements using a custom MinHeap.

    Parameters:
        nums (list[int]): Input array
        k (int): Number of largest elements to extract

    Returns:
        list[int]: k largest elements sorted in descending order
    """
    heap = MinHeap()

    # 1. Build heap with first k elements → O(k log k)
    for num in nums[:k]:
        heap.push(num)

    # 2. Process remaining elements → O((n-k) log k)
    for num in nums[k:]:
        if num > heap.peek():
            heap.replace(num)

    # 3. Extract all k elements from heap → O(k log k)
    result = []
    while heap.heap:
        result.append(heap.pop())

    # 4. Result is ascending (min-heap), reverse for descending
    return result[::-1]


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print("Using heapq:", k_largest(arr, k))  # [6, 5]
    print("Using custom heap:", k_largest_custom(arr, k))  # [6, 5]


# -------------------------------
# Using Quick Select algorithm
# -------------------------------

# Python program to find the k largest elements in the array
# using partitioning step of quick sort


# Function to partition the array around a pivot
def partition(arr, left, right):

    # Last element is chosen as a pivot.
    pivot = arr[right]
    i = left

    for j in range(left, right):

        # Elements greater than or equal to pivot
        # are placed in the left side of pivot
        if arr[j] >= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    # The correct sorted position of the pivot
    return i


def quickSelect(arr, left, right, k):
    if left <= right:
        pivotIdx = partition(arr, left, right)

        # Count of all elements in the left part
        leftCnt = pivotIdx - left + 1

        # If leftCnt is equal to k, then we have
        # found the k largest element
        if leftCnt == k:
            return

        # Search in the left subarray
        if leftCnt > k:
            quickSelect(arr, left, pivotIdx - 1, k)

        # Reduce the k by number of elements already covered
        # and search in the right subarray
        else:
            quickSelect(arr, pivotIdx + 1, right, k - leftCnt)


def kLargest(arr, k):
    quickSelect(arr, 0, len(arr) - 1, k)

    # First k elements of the array, will be the largest
    res = arr[:k]

    # Sort the result in descending order
    res.sort(reverse=True)
    return res


if __name__ == "__main__":
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    res = kLargest(arr, k)
    print(" ".join(map(str, res)))
