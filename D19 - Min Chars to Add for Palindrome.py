"""
Link :  https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/minimum-characters-to-be-added-at-front-to-make-string-palindrome

Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.

Examples:

Input: s = "abc"
Output: 2
Explanation: Add 'b' and 'c' at front of above string to make it palindrome : "cbabc"
Input: s = "aacecaaaa"
Output: 2
Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"
Constraints:
1 <= s.size() <= 106
"""


class Solution:
    def minChar(self, s: str) -> int:
        """
        Returns the minimum number of characters that need to be added at the
        beginning of the string to make it a palindrome.

        Approach:
        - Use KMP prefix table on the string: s + '&' + reversed(s)
        - The longest prefix which is also suffix gives the largest palindromic prefix
        - Minimum characters = len(s) - longest palindromic prefix

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        def compute_lps(combined: str) -> int:
            lps = [0] * len(combined)
            prefix = 0  # prefix pointer
            suffix = 1  # suffix pointer

            while suffix < len(combined):
                if combined[prefix] == combined[suffix]:
                    prefix += 1
                    lps[suffix] = prefix
                    suffix += 1
                else:
                    if prefix == 0:
                        suffix += 1
                    else:
                        prefix = lps[prefix - 1]

            return lps[-1]  # longest palindromic prefix

        # Build the combined string
        combined = s + "&" + s[::-1]

        longest_palindromic_prefix = compute_lps(combined)

        return len(s) - longest_palindromic_prefix
