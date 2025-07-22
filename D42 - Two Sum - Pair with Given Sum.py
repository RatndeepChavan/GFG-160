"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/key-pair5616


Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

Examples:

Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: arr[3] + arr[4] = -3 + 1 = -2
Input: arr[] = [1, -2, 1, 0, 5], target = 0
Output: false
Explanation: None of the pair makes a sum of 0
Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[]

Constraints:
1 ≤ arr.size ≤ 105
-105 ≤ arr[i] ≤ 105
-2*105 ≤ target ≤ 2*105
"""


class Solution:
    def twoSum(self, arr, target):
        """
        Determines if any two distinct elements in the array sum up to the given target.

        ✅ Approach:
        - Traverse the array once.
        - For each element, compute the difference between target and the current value.
        - Use a set to store previously seen values for O(1) lookups.
        - If the required value is already in the set, a valid pair exists.

        ⏱️ Time: O(N), where N is the length of the array
        🧠 Space: O(N), due to the extra set used for lookups
        """

        n = len(arr)

        # ! If array has less than 2 elements, no valid pair is possible
        if n < 2:
            return False

        # ! Edge case: If array has exactly 2 elements, check their sum
        if n == 2:
            return sum(arr) == target

        value_tracker = set()  # Tracks seen values

        for current_value in arr:
            required_value = target - current_value

            # Check if the complement value was seen earlier
            if required_value in value_tracker:
                return True

            # Store the current value for future lookups
            value_tracker.add(current_value)

        # If loop completes with no match, return False
        return False
