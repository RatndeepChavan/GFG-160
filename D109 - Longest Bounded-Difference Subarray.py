"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/queue-and-deque-gfg-160/problem/longest-bounded-difference-subarray

Given an array of positive integers arr[] and a non-negative integer x, the task is to find the longest sub-array where the absolute difference between any two elements is not greater than x.
If multiple such subarrays exist, return the one that starts at the smallest index.

Examples:

Input: arr[] = [8, 4, 5, 6, 7], x = 3 
Output: [4, 5, 6, 7] 
Explanation: The sub-array described by index [1..4], i.e. [4, 5, 6, 7]
contains no two elements whose absolute difference is greater than 3.

Input: arr[] = [1, 10, 12, 13, 14], x = 2 
Output: [12, 13, 14] 
Explanation: The sub-array described by index [2..4], i.e. [12, 13, 14]
contains no two elements whose absolute difference is greater than 2. 

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109
0 ≤ x ≤ 109
"""

# ------------------------------------------------------------------
# * 🟢 Optimized Sliding Window + Monotonic Deques (O(N))
# ------------------------------------------------------------------

from collections import deque

class SolutionDeque:
    """
    🧠 Problem:
    -----------
    Find the longest contiguous subarray such that:
        max(subarray) - min(subarray) ≤ x

    💡 Approach:
    ------------
    - Maintain two **deques**:
        1️⃣ `max_dq`: decreasing order → tracks current window's maximum
        2️⃣ `min_dq`: increasing order → tracks current window's minimum
    - Use **two pointers** (`left`, `right`) for sliding window.
    - Expand window by moving `right`.
    - Shrink window from `left` whenever `max - min > x`.

    ⚙️ Steps:
    ----------
    1. For each `arr[right]`, maintain both deques.
    2. If window condition breaks (difference > x), move `left` ahead.
    3. Keep track of best window (length & start).

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N) — each element added/removed at most once  
    🧠 **Space:** O(k) — for deques

    ✅ Optimal solution — fast, clean, and elegant.
    """

    def longestSubarray(self, arr, x):
        min_dq, max_dq = deque(), deque()
        left = best_start = best_len = 0

        for right in range(len(arr)):
            # 🧱 Maintain decreasing order in max_dq
            while max_dq and arr[max_dq[-1]] < arr[right]:
                max_dq.pop()
            max_dq.append(right)

            # 🧩 Maintain increasing order in min_dq
            while min_dq and arr[min_dq[-1]] > arr[right]:
                min_dq.pop()
            min_dq.append(right)

            # 🚪 Shrink window if condition breaks
            while arr[max_dq[0]] - arr[min_dq[0]] > x:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()

            # ✅ Update best window
            curr_len = right - left + 1
            if curr_len > best_len:
                best_len = curr_len
                best_start = left

        # Return longest valid subarray
        return arr[best_start: best_start + best_len]

# ------------------------------------------------------------------
# * 🟡 Brute Force (Naïve Approach — O(N²))
# ------------------------------------------------------------------

class SolutionBruteForce:
    """
    🧩 Approach:
    ------------
    - For each starting point `i`, expand window to the right.
    - Track `min_val` and `max_val` for the current window.
    - Stop expanding when `max_val - min_val > x`.

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N²)
    🧠 **Space:** O(1)
    """

    def longestSubarray(self, arr, x):
        n = len(arr)
        best_start = best_len = 0

        for i in range(n):
            min_val = max_val = arr[i]
            for j in range(i, n):
                min_val = min(min_val, arr[j])
                max_val = max(max_val, arr[j])

                if max_val - min_val <= x:
                    if j - i + 1 > best_len:
                        best_len = j - i + 1
                        best_start = i
                else:
                    break  # further expansion will only worsen diff

        return arr[best_start: best_start + best_len]


# ------------------------------------------------------------------
# * 🔴 Heap-Based Sliding Window (Conceptual Variant)
# ------------------------------------------------------------------

import heapq

class SolutionHeap:
    """
    🧩 Idea:
    --------
    - Maintain two heaps:
        🔺 Max-Heap for window maximums
        🔻 Min-Heap for window minimums
    - Slide the window using `left` and `right` pointers.
    - Pop invalid elements (outside window) as needed.

    ⚠️ Drawback:
    -------------
    - Heap cannot efficiently remove arbitrary elements (lazy deletion needed).
    - Hence, complexity can degrade in practice.

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N log N)
    🧠 **Space:** O(N)
    """

    def longestSubarray(self, arr, x):
        max_heap, min_heap = [], []
        left = best_start = best_len = 0

        for right, val in enumerate(arr):
            heapq.heappush(max_heap, (-val, right))
            heapq.heappush(min_heap, (val, right))

            # Adjust left pointer until condition satisfied
            while -max_heap[0][0] - min_heap[0][0] > x:
                left += 1
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            curr_len = right - left + 1
            if curr_len > best_len:
                best_len = curr_len
                best_start = left

        return arr[best_start: best_start + best_len]
