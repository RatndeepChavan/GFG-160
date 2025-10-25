"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/longest-valid-parentheses5657

Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
The closing parenthesis must be after its opening parenthesis.

Examples :
Input: s = "((()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Input: s = ")()())"
Output: 4
Explanation: The longest valid parenthesis substring is "()()".
Input: s = "())()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".

Constraints:
1 ≤ s.size() ≤ 106  
s consists of '(' and ')' only
"""


# ------------------------------------------------------------------
# * 🟢 1. Stack Approach
# ------------------------------------------------------------------
class SolutionStack:
    """
    🧩 Approach:
    ------------
    - Use a stack to track indices of unmatched parentheses.
    - Start with -1 in stack (acts as a base for valid substrings).
    - For every '(' → push its index.
    - For every ')' → pop.
        * If stack non-empty → valid length = idx - stack[-1].
        * If stack empty → push current index as new base.

    📊 Complexity:
    --------------
    - ⏱️ Time: O(N)
    - 🧠 Space: O(N)

    ✅ Most intuitive approach.
    """

    def maxLength(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, idx - stack[-1])
                else:
                    stack.append(idx)

        return max_len


# ------------------------------------------------------------------
# * 🟡 2. Dynamic Programming (DP)
# ------------------------------------------------------------------
class SolutionDP:
    """
    🧩 Approach:
    ------------
    - Maintain a dp[] array where dp[i] = length of longest valid substring ending at i.
    - If s[i] == ')' and s[i-1] == '(' → dp[i] = dp[i-2] + 2
    - If s[i] == ')' and s[i-1] == ')' → check matching '(' at i - dp[i-1] - 1.

    📊 Complexity:
    --------------
    - ⏱️ Time: O(N)
    - 🧠 Space: O(N)

    ✅ Good alternative when DP is allowed, avoids explicit stack.
    """

    def maxLength(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
                max_len = max(max_len, dp[i])

        return max_len


# ------------------------------------------------------------------
# * 🔴 3. Two-Pass Counter (Greedy Scan)
# ------------------------------------------------------------------
class SolutionTwoPass:
    """
    🧩 Approach:
    ------------
    - Scan left → right:
        * Track count of '(' and ')'.
        * If counts equal → update max_len.
        * If ')' > '(' → reset counters.
    - Scan right → left (mirror pass) to handle cases like "(()".

    📊 Complexity:
    --------------
    - ⏱️ Time: O(N)
    - 🧠 Space: O(1)

    ✅ Space-optimal, elegant trick.
    """

    def maxLength(self, s: str) -> int:
        left = right = max_len = 0

        # Left → Right pass
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Right → Left pass
        left = right = 0
        for char in reversed(s):
            if char == ")":
                right += 1
            else:
                left += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len
