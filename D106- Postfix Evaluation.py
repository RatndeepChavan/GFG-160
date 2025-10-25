"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/evaluation-of-postfix-expression1735

You are given an array of strings arr[] that represents a valid arithmetic expression written in Reverse Polish Notation (Postfix Notation). Your task is to evaluate the expression and return an integer representing its value.

Note: A postfix expression is of the form operand1 operand2 operator (e.g., "a b +"). 
And the division operation between two integers always computes the floor value, i.e floor(5 / 3) = 1 and floor(-5 / 3) = -2.
It is guaranteed that the result of the expression and all intermediate calculations will fit in a 32-bit signed integer.

Examples:
Input: arr[] = ["2", "3", "1", "*", "+", "9", "-"]
Output: -4
Explanation: If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.

Input: arr[] = ["2", "3", "^", "1", "+"]
Output: 9
Explanation: If the expression is converted into an infix expression, it will be 2 ^ 3 + 1 = 8 + 1 = 9.

Constraints:
3 ≤ arr.size() ≤ 103
arr[i] is either an operator: "+", "-", "*", "/" or "^", or an integer in the range [-104, 104]
"""

# ------------------------------------------------------------------
# * 🧮 Evaluate Postfix Expression (Reverse Polish Notation)
# ------------------------------------------------------------------
class Solution:
    """
    🧩 Problem:
    ------------
    Evaluate a postfix (Reverse Polish) expression where operands
    and operators are given as a list of strings.

    Example:
        Input  ➜ ["2", "3", "1", "*", "+", "9", "-"]
        Output ➜ -4
        Explanation:
            2 + (3 * 1) - 9 = -4

    💡 Approach:
    -------------
    - Use a stack to store operands.
    - When encountering an operator:
        1️⃣ Pop top two operands (val2, val1)
        2️⃣ Apply the operator ➜ (val1 op val2)
        3️⃣ Push result back to stack.
    - At the end, the stack will contain a single result.

    🧠 Key Insight:
    ----------------
    Postfix eliminates parentheses — evaluation order is **naturally determined**
    by operand placement, not operator precedence.

    📊 Complexity:
    --------------
    - ⏱️ **Time:** O(N)   (each token processed once)
    - 🧠 **Space:** O(N)  (stack for operands)
    """

    def evaluatePostfix(self, arr):
        stack = []
        operators = {"+", "-", "*", "/", "^"}

        for token in arr:
            # * Case 1: Operand → push it to stack
            if token not in operators:
                stack.append(int(token))

            # * Case 2: Operator → pop top 2, evaluate, push result
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+": 
                    stack.append(val1 + val2)
                elif token == "-": 
                    stack.append(val1 - val2)
                elif token == "*": 
                    stack.append(val1 * val2)
                elif token == "/": 
                    # ❓ Integer division (as per GFG spec)
                    # Ensures truncation toward 0
                    stack.append(int(val1 / val2))
                elif token == "^": 
                    stack.append(val1 ** val2)

        # Final result remains at top
        return stack[-1]
