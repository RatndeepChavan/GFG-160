"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/parenthesis-checker2744

Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
An expression is balanced if:

Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order.

Examples :
Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.

Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.

Constraints:
1 ≤ s.size() ≤ 106
s[i] ∈ {'{', '}', '(', ')', '[', ']'}
"""


# ------------------------------------------------------------------
# * 🟢 1. Stack storing expected closings
# ------------------------------------------------------------------
class SolutionExpectedClosing:
    """
    🧩 Approach:
    ------------
    - Push the *expected* closing bracket whenever you see an opening.
    - When a closing comes → check it matches the stack top.
    - At the end, stack must be empty.

    ✅ Very direct, avoids extra mapping lookup.
    """

    def isBalanced(self, s: str) -> bool:
        tracker = []

        for char in s:
            if char == "(":
                tracker.append(")")
            elif char == "[":
                tracker.append("]")
            elif char == "{":
                tracker.append("}")
            elif tracker and char == tracker[-1]:
                tracker.pop()
            else:
                return False

        return not tracker


# ------------------------------------------------------------------
# * 🟡 2. Hash map + stack of openings
# ------------------------------------------------------------------
class SolutionWithHash:
    """
    🧩 Approach:
    ------------
    - Maintain a hash map of matching pairs:
        mapping = {')':'(', ']':'[', '}':'{'}
    - Push opening brackets to stack.
    - On closing:
        * Stack must not be empty.
        * Stack top must equal mapping[closing].
    - End with empty stack.

    ✅ Classic textbook solution.
    """

    def isBalanced(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in mapping.values():      # opening bracket
                stack.append(char)
            elif char in mapping:             # closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False   # invalid character

        return not stack


# ------------------------------------------------------------------
# * 🔴 3. Hash map + direct matching (shorter form)
# ------------------------------------------------------------------
class SolutionWithHashShort:
    """
    🧩 Approach:
    ------------
    - Same as #2 but flips mapping:
        mapping = {'(':')', '[':']', '{':'}'}
    - Push only openings.
    - On closing:
        * Check stack non-empty AND top opening's matching == current closing.

    ✅ Cleaner, shorter, popular in interviews.
    """

    def isBalanced(self, s: str) -> bool:
        mapping = {'(':')', '[':']', '{':'}'}
        stack = []

        for char in s:
            if char in mapping:              # opening
                stack.append(char)
            elif not stack or mapping[stack.pop()] != char:
                return False

        return not stack
