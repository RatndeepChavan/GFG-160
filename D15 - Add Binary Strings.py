"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/add-binary-strings3805

Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
------
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation:
  100
+  10
------
  110

Constraints:
1 ≤s1.size(), s2.size()≤ 106
"""


class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.

        Approach:
        - Trim leading zeros from both strings
        - Iterate from end (LSB to MSB), add digits and carry
        - Reverse and join the result for final output

        Args:
            s1 (str): First binary number as string
            s2 (str): Second binary number as string

        Returns:
            str: Sum of s1 and s2 in binary representation

        Time Complexity: O(max(n, m)), where n and m are lengths of s1 and s2
        Space Complexity: O(max(n, m)), for the result list
        """

        def trim_leading_zeros(s: str) -> str:
            index_of_one = s.find("1")
            return s[index_of_one:] if index_of_one != -1 else "0"

        # Step 1: Trim leading zeros
        s1 = trim_leading_zeros(s1)
        s2 = trim_leading_zeros(s2)

        # Ensure s1 is always the longer string
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        len1 = len(s1)
        len2 = len(s2)

        i = len1 - 1
        j = len2 - 1
        carry = 0
        result = []

        # Step 2: Add from the end of both strings
        while i >= 0:
            bit_sum = int(s1[i]) + carry

            if j >= 0:
                bit_sum += int(s2[j])
                j -= 1

            result.append(str(bit_sum % 2))
            carry = bit_sum // 2
            i -= 1

        # Step 3: Handle leftover carry
        if carry:
            result.append("1")

        # Step 4: Reverse and join result
        return "".join(reversed(result))
