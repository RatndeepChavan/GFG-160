"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote

You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array.

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: 0 candidate occur more than n/3 times.

Constraint:
1 <= arr.size() <= 106
-109 <= arr[i] <= 109
"""


class Solution:
    def findMajority(self, arr):
        """
        Uses the Boyer-Moore Voting Algorithm (n/3 version) to find all elements
        that appear more than ⌊n/3⌋ times.

        Args:
            arr (List[int]): The input array.

        Returns:
            List[int]: List of majority elements, sorted in ascending order.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)

        # Step 1: Find potential candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []
        count1 = count2 = 0

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return sorted(result)
