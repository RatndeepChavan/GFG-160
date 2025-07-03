"""
Link - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
"""


class Solution:
    def getSecondLargest(self, arr):
        """
        Finds the second largest distinct element in an array of positive integers.

        Approach:
        - Initialize two variables: first_largest and second_largest.
        - Traverse the array:
            - If current element is greater than first_largest:
                - Update second_largest to first_largest.
                - Update first_largest to current element.
            - Else if element is less than first_largest and greater than second_largest:
                - Update second_largest.
        - Return second_largest. If no valid second largest exists, return -1.

        Args:
            arr (List[int]): Array of positive integers.

        Returns:
            int: Second largest element if it exists, else -1.

        Time Complexity: O(n), where n is the length of the array.
        Space Complexity: O(1), as we are using constant extra space.
        """

        first_largest = second_largest = (
            -1
        )  # Assumes only positive integers, per constraints

        for num in arr:
            if num > first_largest:
                first_largest, second_largest = num, first_largest
            elif first_largest > num > second_largest:
                second_largest = num

        return second_largest
