"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/check-if-strings-are-rotations-of-each-other-or-not-1587115620

You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.

Note: The characters in the strings are in lowercase.

Examples :

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.
Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.
Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.

Constraints:
1 <= s1.size(), s2.size() <= 105
"""


class Solution:
    def areRotations(self, s1: str, s2: str) -> bool:
        """
        Checks whether s1 is a rotation of s2.

        Logic:
        - If two strings are of equal length and s1 is a rotation of s2,
          then s1 must appear as a substring in s2 + s2.

        Args:
            s1 (str): First string
            s2 (str): Second string

        Returns:
            bool: True if s1 is a rotation of s2, False otherwise
        """
        # return s1 in (s2 + s2) # short and sweet

        # Step 1: Check length equality
        if len(s1) != len(s2):
            return False

        # Step 2: Create a temporary string by doubling s2
        temp = s2 + s2

        # Step 3: Check if s1 appears in the doubled string
        return s1 in temp
