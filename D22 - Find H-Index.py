"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/find-h-index--165609

Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.

H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.

Examples:

Input: citations[] = [3, 0, 5, 3, 0]
Output: 3
Explanation: There are at least 3 papers (3, 5, 3) with at least 3 citations.
Input: citations[] = [5, 1, 2, 4, 1]
Output: 2
Explanation: There are 3 papers (with citation counts of 5, 2, and 4) that have 2 or more citations. However, the H-Index cannot be 3 because there aren't 3 papers with 3 or more citations.
Input: citations[] = [0, 0]
Output: 0
Constraints:
1 ≤ citations.size() ≤ 106
0 ≤ citations[i] ≤ 106
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Computes the H-index using counting (bucket sort) approach.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(citations)
        freq = [0] * (n + 1)

        # Step 1: Count citations, bucket everything >= n into freq[n]
        for c in citations:
            if c >= n:
                freq[n] += 1
            else:
                freq[c] += 1

        # Step 2: Iterate from n to 0 and find the highest h satisfying the condition
        papers_with_at_least = 0
        h = n

        while h >= 0:
            papers_with_at_least += freq[h]
            if papers_with_at_least >= h:
                return h
            h -= 1

        return 0
