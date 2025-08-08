"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/longest-distinct-characters-in-string5848

Given a string s, find the length of the longest substring with all distinct characters.

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.
Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.
Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.

Constraints:
1<= s.size()<=3*104
All the characters are in lowercase
"""


class Solution:
    def longestUniqueSubstr(self, s):
        """
        ✅ Approach:
        - Use a sliding window with two pointers `left` and `right`.
        - Maintain a hash map to store the last seen index of each character.
        - If a repeating character is found within the current window, shift the left pointer just after the last occurrence.
        - Continuously track and update the maximum length.

        ⏱️ Time: O(N), where N is the length of the string
        🧠 Space: O(1), at most 26 entries in the map
        """

        left = -1  # start point of the current window
        right = 0  # End point of the current window

        tracker = {}  # Tracks the last seen index of each character

        substring_len = 0  # Stores maximum length found so far
        current_len = 0  # Length of current window

        while right < len(s):
            alphabet = s[right]
            previous_idx = tracker.get(alphabet)

            # ! If the current character was seen and is inside the current window
            if previous_idx is not None and left < previous_idx:
                # Shrink the window from the left
                left = previous_idx

            # Update the current window length
            current_len = right - left
            # Update the answer if needed
            substring_len = max(substring_len, current_len)

            # Store/update last seen index of current character
            tracker[alphabet] = right
            right += 1  # Expand the window

        return substring_len
