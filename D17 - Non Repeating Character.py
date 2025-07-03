"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/non-repeating-character-1587115620

Given a string s consisting of lowercase English Letters. Return the first non-repeating character in s.
If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.
Input: s = "aabbccc"
Output: -1
Explanation: All the characters in the given string are repeating.

Constraints:
1 ≤ s.size() ≤ 105
"""


class Solution:
    def nonRepeatingChar(self, s: str) -> str:
        """
        Returns the first non-repeating character in the string.
        If no such character exists, returns '-1'.

        Time Complexity: O(n)
        Space Complexity: O(1)  # Only 26 letters (assuming lowercase English)

        Args:
            s (str): The input string.

        Returns:
            str: First non-repeating character or -1
        """
        freq = {}

        # Step 1: Count frequencies
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Step 2: Find the first character with count == 1
        for char in s:
            if freq[char] == 1:
                return char

        return "-1"
