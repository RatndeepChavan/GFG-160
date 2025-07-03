"""
Link - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array

You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.

Constraints:
1<=arr.size()<=105
0<=arr[i]<=105
"""


class Solution:
    def reverseArray(self, arr):
        """
        Reverses the elements of the given array in-place using a two-pointer approach.

        Approach:
        We use two pointers: `left` starting from the beginning of the array,
        and `right` starting from the end. We swap the elements at these positions
        and move the pointers towards each other until they meet or cross.

        This technique ensures that the array is reversed in-place without using
        any extra space.

        Args:
            arr (List[int]): The input array to be reversed.

        Returns:
            List[int]: The same array with elements reversed.

        Time Complexity: O(n), where n is the length of the array.
        Space Complexity: O(1), as the reversal is done in-place.
        """
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
