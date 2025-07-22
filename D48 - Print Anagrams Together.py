"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/print-anagrams-together

Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be arranged in the order of their appearance in the original array. Refer to the sample case for clarification.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation:
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.

Constraints:
1<= arr.size() <=100
1<= arr[i].size() <=10
"""


class Solution:
    def anagrams(self, arr):
        """
        Groups anagrams from the given list of words.

        ✅ Approach:
        - For each word, sort its characters to form a key.
        - Store all words with the same sorted key in a dictionary (anagram groups).
        - Return the list of grouped anagrams.

        ⏱️ Time: O(N * K log K), where N is the number of words and K is the average word length (due to sorting).
        🧠 Space: O(N * K), for storing the grouped words.
        """
        anagrams_tracker = {}  # Dictionary to group words with same sorted structure

        for word in arr:
            # ? Sorting characters gives unique key for anagram groups
            sorted_word = "".join(sorted(word))

            # Add word to the appropriate group
            if sorted_word in anagrams_tracker:
                anagrams_tracker[sorted_word].append(word)
            else:
                anagrams_tracker[sorted_word] = [word]

        # Extract all grouped anagrams as a list of lists
        return list(anagrams_tracker.values())
