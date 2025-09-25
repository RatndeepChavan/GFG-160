"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/recursion-and-backtracking-gfg-160/problem/permutations-of-a-given-string2041

Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

Examples:

Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.
Input: s = "ABSG"
Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
Explanation: Given string ABSG has 24 unique permutations.
Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.

Constraints:
1 <= s.size() <= 9
s contains only Uppercase english alphabets
"""


class Solution:
    def findPermutation(self, s):
        """
        ✅ Generates all unique permutations of the input string.

        Plain English Approach:
        ------------------------
        * If the string has only one character, it's the only permutation.
        * Otherwise, for each character in the string:
            - Fix that character at the beginning.
            - Recursively generate all permutations of the remaining string.
            - Combine the fixed character with each of the sub-permutations.
        * Use a set to avoid duplicates in case the input has repeated characters.
        * Return the final result as a list.

        Args:
            s (str): Input string.

        Returns:
            List[str]: List of unique permutations.

        ⏱️ Time Complexity: O(N! * N) — N! permutations, each of length N.
        🧠 Space Complexity: O(N!) — For storing all permutations in a set/list.
        """

        def get_permutations(string):
            if len(string) == 1:
                return [string]

            result = set()
            for i in range(len(string)):
                remaining = string[:i] + string[i + 1 :]
                for sub in get_permutations(remaining):
                    result.add(string[i] + sub)
            return result

        return list(get_permutations(s))


"""
? Generator-Based Recursive Permutations (Without Counter)
class Solution:
    def findPermutation(self, s):
        '''
        ✅ Approach (Recursive Generator without Counter):
        - Classic backtracking using recursion.
        - Yields permutations one-by-one using `yield` (memory efficient).
        - Handles duplicates naturally (but doesn't remove them).

        ⚠️ Will generate duplicate permutations if `s` has repeated characters.

        ⏱️ Time: O(N!) — number of permutations
        🧠 Space: O(N) — max call stack depth and temp list
        '''

        def generate(chars, path):
            if not chars:
                yield ''.join(path)
                return

            for i in range(len(chars)):
                # ? Choose one char at index i
                new_chars = chars[:i] + chars[i+1:]
                path.append(chars[i])
                yield from generate(new_chars, path)
                path.pop()

        yield from generate(list(s), [])

"""


"""
?  Iterative Permutation Generator (Custom, Stack-Safe)
class Solution:
    def findPermutation(self, s):
        '''
        ✅ Approach (Iterative Generator with Stack Simulation):
        - Simulate the recursive backtracking process using an explicit stack.
        - Avoid recursion (stack-safe for large inputs).
        - Generate permutations one-by-one using `yield` (memory-efficient).

        ✅ Why it matters:
        - Suitable for long strings (no RecursionError).
        - Suitable for pipelines/streaming huge outputs.
        - Pure Python — no itertools used.

        ⏱️ Time: O(N!) — all permutations must be visited
        🧠 Space: O(N) per frame, O(N!) total if all results stored externally

        * Duplicates are skipped using frequency counting.
        '''

        from collections import Counter

        counter = Counter(s)
        length = len(s)
        stack = [([], counter)]

        while stack:
            path, freq = stack.pop()

            if len(path) == length:
                yield ''.join(path)
                continue

            for ch in sorted(freq.keys(), reverse=True):  # reverse for correct order due to stack pop
                if freq[ch] > 0:
                    new_freq = freq.copy()
                    new_freq[ch] -= 1
                    stack.append((path + [ch], new_freq))

"""


"""
? Generator-Based Recursive Permutation
class Solution:
    def findPermutation(self, s):
        '''
        ✅ Approach (Recursive Generator):
        - Use backtracking-style recursion with a generator (yield).
        - Swap characters in-place to build permutations step-by-step.
        - Use a set at each level to avoid duplicate permutations due to repeated characters.
        - Fully custom, no itertools used.

        ✅ Why a generator?
        - Outputs one permutation at a time.
        - Avoids building/storing a huge result list in memory.
        - Useful for streaming or pipelining.

        ⏱️ Time: O(N!) to generate all permutations
        🧠 Space: O(N) recursion depth + some space for deduplication
        '''
        def backtrack(path, counter):
            if len(path) == len(s):
                yield ''.join(path)
                return
            for ch in counter:
                if counter[ch] > 0:
                    path.append(ch)
                    counter[ch] -= 1

                    yield from backtrack(path, counter)

                    # Backtrack
                    counter[ch] += 1
                    path.pop()

        # Count frequency of characters to handle duplicates
        from collections import Counter
        counter = Counter(s)

        return backtrack([], counter)
"""

"""
! SHORT AND SWEET PYTHONIC SOLUTION
from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Generate all permutations as tuples
        perms = set(permutations(s))

        # Join each tuple into a string and sort the result
        return sorted(''.join(p) for p in perms)
"""
