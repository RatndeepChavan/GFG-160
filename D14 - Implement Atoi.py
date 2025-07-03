"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/implement-atoi

Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
Examples:

Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer
Input: s = "  -"
Output: 0
Explanation: No digits are present, therefore the returned answer is 0.
Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number will be greater than 231 – 1, therefore print 231 – 1 = 2147483647.
Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.
Input: s = "  -0012gfg4"
Output: -12
Explanation: Nothing is read after -12 as a non-digit character ‘g’ was encountered.

Constraints:
1 ≤ |s| ≤ 15
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer using rules similar to C/C++'s atoi function.

        Rules:
        - Skip leading whitespaces.
        - Check for optional '+' or '-' sign.
        - Read digits until non-digit character or end of string.
        - Clamp result to 32-bit signed integer range [-2^31, 2^31 - 1].

        Args:
            s (str): Input string

        Returns:
            int: Parsed integer value, clamped within bounds

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Step 1: Skip leading whitespaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Handle optional sign
        if i < n and s[i] in {"-", "+"}:
            sign = -1 if s[i] == "-" else 1
            i += 1

        # Step 3: Convert digits to number
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            result = result * 10 + digit

            # Step 4: Clamp if out of bounds
            if result > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN

            i += 1

        return sign * result
