"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/search-pattern0205

Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices.
Note: Return an empty list in case of no occurrences of pattern.

Examples :

Input: txt = "abcab", pat = "ab"
Output: [0, 3]
Explanation: The string "ab" occurs twice in txt, one starts at index 0 and the other at index 3.
Input: txt = "abesdu", pat = "edu"
Output: []
Explanation: There's no substring "edu" present in txt.
Input: txt = "aabaacaadaabaaba", pat = "aaba"
Output: [0, 9, 12]
Explanation:

Constraints:
1 ≤ txt.size() ≤ 106
1 ≤ pat.size() < txt.size()
Both the strings consist of lowercase English alphabets.
"""


class Solution:
    def search(self, pat: str, txt: str) -> list[int]:
        """
        Finds all occurrences of `pat` in `txt` using the KMP algorithm.

        Returns:
            List[int]: List of starting indices (0-based) where `pat` is found.

        Time Complexity: O(n + m)
        Space Complexity: O(m)
        """

        def compute_lps(pattern: str) -> list[int]:
            """
            Builds the LPS (Longest Prefix Suffix) array using a while loop for clarity.
            lps[i] = the length of the longest proper prefix of pattern[0..i]
                    which is also a suffix of that substring.
            """
            lps = [0] * len(pattern)
            prefix = 0
            suffix = 1

            while suffix < len(pattern):
                if pattern[suffix] == pattern[prefix]:
                    prefix += 1
                    lps[suffix] = prefix
                    suffix += 1
                else:
                    if prefix != 0:
                        prefix = lps[prefix - 1]  # backtrack
                    else:
                        lps[suffix] = 0
                        suffix += 1

            return lps

        n = len(txt)
        m = len(pat)
        result = []
        lps = compute_lps(pat)

        text_index = pattern_index = 0

        while text_index < n:
            if txt[text_index] == pat[pattern_index]:
                text_index += 1
                pattern_index += 1

            if pattern_index == m:
                result.append(text_index - pattern_index)
                pattern_index = lps[pattern_index - 1]

            elif text_index < n and txt[text_index] != pat[pattern_index]:
                if pattern_index != 0:
                    pattern_index = lps[pattern_index - 1]
                else:
                    text_index += 1

        return result
