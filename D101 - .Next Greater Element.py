"""
Lnk : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/next-larger-element-1587115620

You are given an array arr[] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1.

Examples
Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.
Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1, for 1 it is 3 and then for 3 there is no larger element on right and hence -1.
Input: arr[] = [1, 2, 3, 5]
Output: [2, 3, 5, -1]
Explanation: For a sorted array, the next element is next greater element also except for the last element.
Input: arr[] = [5, 4, 3, 1]
Output: [-1, -1, -1, -1]
Explanation: There is no next greater element for any of the elements in the array, so all are -1.

Constraints:
1 ≤ arr.size() ≤ 106
"""

# ------------------------------------------------------------------
# * 🟢 1. Monotonic Stack (Right → Left)
# ------------------------------------------------------------------
class SolutionStack:
    """
    🧩 Approach:
    ------------
    - Traverse from right → left.
    - Maintain a *monotonic decreasing stack* of "candidates".
    - For each arr[i]:
        * Pop elements ≤ arr[i] (since they can't be the "next greater").
        * Top of stack (if exists) = answer.
        * Push arr[i] into stack.

    📊 Complexity:
    --------------
    - ⏱️ Time: O(N)   (each element pushed & popped at most once)
    - 🧠 Space: O(N) (stack for candidates)

    ✅ Most optimal & widely used method.
    """

    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []  # monotonic decreasing stack

        for i in range(n - 1, -1, -1):  # traverse backwards
            while stack and arr[i] >= stack[-1]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(arr[i])

        return res


# ------------------------------------------------------------------
# * 🟡 2. Brute Force
# ------------------------------------------------------------------
class SolutionBrute:
    """
    🧩 Approach:
    ------------
    - For every element arr[i], look to the right until you find a greater element.
    - If found → answer = that element, else -1.

    📊 Complexity:
    --------------
    - ⏱️ Time: O(N²)
    - 🧠 Space: O(1)

    ❌ Too slow for large arrays, but useful for understanding the problem.
    """

    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n

        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    res[i] = arr[j]
                    break
        return res


# ------------------------------------------------------------------
# * 🔴 3. Using HashMap + Stack (LeetCode 496 style)
# ------------------------------------------------------------------
class SolutionHashMap:
    """
    🧩 Approach:
    ------------
    - Variant often used when we have "subset array" & need mapping.
    - Traverse arr with stack (like monotonic stack).
    - Build a hashmap: {value -> next greater}.
    - Then map results for original arr.

    📊 Complexity:
    --------------
    - ⏱️ Time: O(N)
    - 🧠 Space: O(N) for hashmap + stack

    ✅ Useful in problems like "Next Greater Element I/II".
    """

    def nextLargerElement(self, arr):
        res = []
        stack = []
        nge_map = {}

        for num in arr:  # left → right traversal
            while stack and num > stack[-1]:
                nge_map[stack.pop()] = num
            stack.append(num)

        # Remaining elements → no next greater
        while stack:
            nge_map[stack.pop()] = -1

        # Build result array
        for num in arr:
            res.append(nge_map[num])

        return res
