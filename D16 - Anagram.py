"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/anagram-1587115620

Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-empty.

Examples :

Input: s1 = "geeks", s2 = "kseeg"
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergic"
Output: false
Explanation: Characters in both the strings are not same, so they are not anagrams.
Input: s1 = "g", s2 = "g"
Output: true
Explanation: Character in both the strings are same, so they are anagrams.

Constraints:
1 ≤ s1.size(), s2.size() ≤ 105
"""


class Solution:
    def areAnagrams(self, s1: str, s2: str) -> bool:
        """
        Checks whether two lowercase strings are anagrams using frequency array.

        Assumptions:
        - Only lowercase letters ('a' to 'z') are present.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(s1) != len(s2):
            return False

        freq = [0] * 26

        for i in range(len(s1)):
            freq[ord(s1[i]) - ord("a")] += 1
            freq[ord(s2[i]) - ord("a")] -= 1

        return all(count == 0 for count in freq)
