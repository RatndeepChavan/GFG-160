"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/queue-and-deque-gfg-160/problem/maximum-of-all-subarrays-of-size-k3101

Given an array arr[] of positive integers and an integer k. You have to find the maximum value for each contiguous subarray of size k. Return an array of maximum values corresponding to each contiguous subarray.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6]
Explanation: 
1st contiguous subarray [1, 2, 3], max = 3
2nd contiguous subarray [2, 3, 1], max = 3
3rd contiguous subarray [3, 1, 4], max = 4
4th contiguous subarray [1, 4, 5], max = 5
5th contiguous subarray [4, 5, 2], max = 5
6th contiguous subarray [5, 2, 3], max = 5
7th contiguous subarray [2, 3, 6], max = 6

Input: arr[] = [5, 1, 3, 4, 2], k = 1
Output: [5, 1, 3, 4, 2]
Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ k ≤ arr.size()
0 ≤ arr[i] ≤ 109
"""


# ------------------------------------------------------------------
# * 🟢 Reverse Traversal + Single Stack (Your Unique Approach)
# ------------------------------------------------------------------

from collections import deque

class SolutionDeque:
    """
    🧩 Approach:
    ------------
    - Maintain a **deque** storing indices of elements in decreasing order of their values.
    - The **front** of deque always holds the index of the largest element in the current window.

    ⚙️ Working:
    -----------
    For each element `arr[i]`:
    1️⃣ Remove indices from front that are **out of the current window** (i - k).  
    2️⃣ Remove from back all indices whose values are **<= current element**, since they’ll never be needed again.
    3️⃣ Append current index to deque.
    4️⃣ Once window size ≥ k, add arr[dq[0]] (front) to result.

    🧠 Why Deque?
    -------------
    - Provides O(1) operations from both ends.
    - Maintains a **monotonic decreasing** sequence of values for each window.

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N) — each element is added/removed at most once  
    🧠 **Space:** O(k) — for deque storage
    """

    def maxOfSubarrays(self, arr, k):
        dq = deque()  # stores indices
        res = []

        for i in range(len(arr)):
            # 🚪 Step 1: Remove elements out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 🧹 Step 2: Maintain decreasing order in deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # ➕ Step 3: Add current index
            dq.append(i)

            # 🧾 Step 4: Record max for each full window
            if i >= k - 1:
                res.append(arr[dq[0]])

        return res


# ------------------------------------------------------------------
# * 🟡 Heap (Max-Heap with Lazy Removal) — O(N log k)
# ------------------------------------------------------------------

import heapq

class SolutionHeap:
    """
    🧩 Approach:
    ------------
    - Use a **max-heap** to store (-value, index) pairs.
    - Each iteration, push the new element and pop from heap while the top index is outside the window.

    💡 Why negative value?
    ----------------------
    - Python’s `heapq` implements a **min-heap**.
    - To simulate a max-heap, we push negative values.

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N log k)  
    🧠 **Space:** O(k)
    """

    def maxOfSubarrays(self, arr, k):
        heap = []  # stores (-value, index)
        res = []

        for i, val in enumerate(arr):
            heapq.heappush(heap, (-val, i))

            # Remove elements out of window
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)

            # Record max
            if i >= k - 1:
                res.append(-heap[0][0])

        return res


# ------------------------------------------------------------------
# * 🔴 Brute Force (Sliding Window Traversal) — O(N·k)
# ------------------------------------------------------------------

class SolutionBruteForce:
    """
    🧩 Approach:
    ------------
    - For each window of size `k`, directly compute the maximum using a loop.
    - Simple but inefficient for large arrays.

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N * k)  
    🧠 **Space:** O(1)
    """

    def maxOfSubarrays(self, arr, k):
        res = []
        n = len(arr)
        for i in range(n - k + 1):
            res.append(max(arr[i:i + k]))
        return res
