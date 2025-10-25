"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/maximum-of-minimum-for-every-window-size3453

You are given an integer array arr[], the task is to find the maximum of minimum values for every window size k where 1≤ k ≤ arr.size().

For each window size k, consider all contiguous subarrays of length k, determine the minimum element in each subarray, and then take the maximum among all these minimums.

Return the results as an array, where the element at index i represents the answer for window size i+1.

Examples :
Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10] 
Explanation: 
Window size 1: minimums are [10, 20, 30, 50, 10, 70, 30], maximum of minimums is 70.
Window size 2: minimums are [10, 20, 30, 10, 10, 30], maximum of minimums is 30.
Window size 3: minimums are [10, 20, 10, 10, 10], maximum of minimums is 20.
Window size 4–7: minimums are [10, 10, 10, 10], maximum of minimums is 10.
Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]
Explanation: 
Window size 1: minimums of  [10], [20], [30], maximum of minimums is 30.
Window size 2: minimums of [10, 20], [20,30], maximum of minimums is 20.
Window size 3: minimums of [10,20,30], maximum of minimums is 10.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106
"""

# ------------------------------------------------------------------
# * 🟢 1. Monotonic Stack (Optimal O(N)) — "Max of Min for Every Window"
# ------------------------------------------------------------------
class SolutionStack:
    """
    🧩 Problem:
    ------------
    Given an array `arr[]`, for every window size `k (1 ≤ k ≤ N)`:
    - Find the *minimum* of all subarrays of length `k`.
    - Then, return the *maximum* of all those minimums.

    Example:
    --------
    arr = [10, 20, 30, 50, 10, 70, 30]
    Output = [70, 30, 20, 10, 10, 10, 10]
             ↑    ↑   ↑   ↑   ↑   ↑   ↑
             k=1  k=2 k=3 k=4 k=5 k=6 k=7

    🧠 Intuition:
    -------------
    For each element:
    - Find how far it can extend *to the left and right* 
      while still being the minimum in that window.
    - That gives us the **window size** for which it is the *minimum element*.
    - Update the result for that window size with the element's value.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N)** — Each element is pushed & popped once.
    - 🧠 **Space: O(N)** — for stacks and helper arrays.
    """

    def maxOfMins(self, arr):
        n = len(arr)
        left = [-1] * n      # Nearest smaller element to LEFT
        right = [n] * n      # Nearest smaller element to RIGHT
        stack = []

        # * STEP 1️⃣ : Compute nearest smaller to left
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # * STEP 2️⃣ : Compute nearest smaller to right
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # * STEP 3️⃣ : Fill result array based on window size
        res = [0] * (n + 1)
        for i in range(n):
            window = right[i] - left[i] - 1  # Window length where arr[i] is minimum
            res[window] = max(res[window], arr[i])

        # * STEP 4️⃣ : Propagate maximums backwards
        # Because smaller windows may not be filled, 
        # and larger windows already guarantee smaller mins.
        for i in range(n - 1, 0, -1):
            res[i] = max(res[i], res[i + 1])

        return res[1:]  # Skip 0th index (no window of size 0)


# ------------------------------------------------------------------
# * 🔸 2. Alternative: Brute Force (for understanding only)
# ------------------------------------------------------------------

class SolutionBruteForce:
    """
    🚧 Brute Force Approach:
    ------------------------
    - For every window size `k`, slide over the array.
    - Compute the min for each window and take its max.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N²)** (nested windows)
    - 🧠 **Space: O(1)**

    ❌ Too slow for large N, but useful for intuition.
    """

    def maxOfMins(self, arr):
        n = len(arr)
        res = []
        for k in range(1, n + 1):
            max_of_mins = float('-inf')
            for i in range(n - k + 1):
                window_min = min(arr[i:i + k])
                max_of_mins = max(max_of_mins, window_min)
            res.append(max_of_mins)
        return res
