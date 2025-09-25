"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/powx-n

Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

Examples:
Input: b = 3.00000, e = 5
Output: 243.00000
Input: b = 0.55000, e = 3
Output: 0.16638
Input: b = -0.67000, e = -7
Output: -16.49971

Constraints:
-100.0 < b < 100.0
-109 <= e <= 109
Either b is not zero or e > 0.
-104 <= be <= 104
"""


class Solution:
    def power(self, b: float, e: int) -> float:
        """
        ✅ Approach: Exponentiation by Squaring (Recursive)
        - Handles negative exponents by taking reciprocal
        - Uses divide-and-conquer:
            - If exponent is even: b^e = (b*b)^(e//2)
            - If exponent is odd:  b^e = b * b^(e-1)
        - Base case: b^0 = 1

        ⏱️ Time: O(log e)
        🧠 Space: O(log e) due to recursion stack
        """

        if b == 0:
            return 0

        def helper(val, exp):
            if exp == 0:
                return 1
            if exp % 2:
                return val * helper(val, exp - 1)
            else:
                return helper(val * val, exp // 2)

        if e < 0:
            return 1 / helper(b, -e)
        else:
            return helper(b, e)
