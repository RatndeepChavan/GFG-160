"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/maximum-rectangular-area-in-a-histogram-1587115620

ou are given a histogram represented by an array arr[ ], where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

Examples:
Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
Largest-Rectangular-Area-in-a-Histogram
Output: 100
Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.

Input: arr[] = [3, 5, 1, 7, 5, 9]
Output: 15
Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.

Input: arr[] = [3]
Output: 3
Explanation: In this example the largest area would be 3 of height 3 and width 1.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104
"""

# ------------------------------------------------------------------
# * 🟢 1. Monotonic Stack (Optimal)
# ------------------------------------------------------------------
class SolutionStack:
    """
    🧩 Approach:
    ------------
    - We maintain a *monotonic increasing stack* of bars (by height).
    - Each element in the stack stores `(start_index, height)`.
    - When a new bar is **shorter** than the top of the stack,
        we pop bars and calculate their area with width = current_index - popped_index.
    - After processing all bars, we calculate areas for remaining bars using total length.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N)**   (each bar is pushed & popped at most once)
    - 🧠 **Space: O(N)**  (stack)

    ✅ Optimal approach — efficient and elegant.
    """

    def getMaxArea(self, arr):
        max_area = 0
        stack = []  # stores tuples: (index, height)

        for idx, ht in enumerate(arr):
            start_idx = idx
            # Pop while current height is smaller → means boundary found for popped bars
            while stack and ht < stack[-1][1]:
                prev_idx, prev_ht = stack.pop()
                width = idx - prev_idx
                max_area = max(max_area, prev_ht * width)
                start_idx = prev_idx  # ? Why update start_idx?
                # Because the popped bar started earlier — current shorter bar inherits that start.
            stack.append((start_idx, ht))

        # Process remaining bars in stack (they extend till end)
        n = len(arr)
        for i, h in stack:
            width = n - i
            max_area = max(max_area, h * width)

        return max_area


# ------------------------------------------------------------------
# * 🟡 2. Brute Force (Naive)
# ------------------------------------------------------------------
class SolutionBrute:
    """
    🧩 Approach:
    ------------
    - For every bar, expand left and right while height >= current bar height.
    - Compute width × height for every position.

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N²)**
    - 🧠 **Space: O(1)**

    ❌ Simple but inefficient for large histograms.
    """

    def getMaxArea(self, arr):
        n = len(arr)
        max_area = 0
        for i in range(n):
            height = arr[i]
            left = right = i

            # Expand left
            while left > 0 and arr[left - 1] >= height:
                left -= 1

            # Expand right
            while right < n - 1 and arr[right + 1] >= height:
                right += 1

            width = right - left + 1
            max_area = max(max_area, width * height)
        return max_area


# ------------------------------------------------------------------
# * 🔴 3. Prefix & Suffix Smaller Element Arrays
# ------------------------------------------------------------------
class SolutionPrefixSuffix:
    """
    🧩 Approach:
    ------------
    - Precompute for each bar:
        🔹 Nearest smaller element on the left
        🔹 Nearest smaller element on the right
    - The width = (right[i] - left[i] - 1)
    - Area = height[i] × width

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(N)**  (two passes)
    - 🧠 **Space: O(N)** (for left[] & right[])

    ✅ Good for understanding relationship with “Next Smaller Element” problems.
    """

    def getMaxArea(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        # * Compute nearest smaller to left
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # * Reset stack for right smaller elements
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # * Compute area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = arr[i] * width
            max_area = max(max_area, area)

        return max_area
