"""
Link - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
"""


class Solution:
    def pushZerosToEnd(self, arr: List[int]) -> None:
        """
        Moves all zeroes in the array to the end while maintaining the relative order of the non-zero elements.

        Approach:
        We use a two-pointer technique to solve this problem efficiently.
        - The `first_ptr` tracks the position of the first zero in the array.
        - The `second_ptr` scans ahead to find the next non-zero element.
        - When a non-zero is found at `second_ptr`, we move it to the position
        pointed by `first_ptr` and place a zero at `second_ptr`.
        - Then, `first_ptr` is advanced to the next zero that needs to be filled.

        This ensures that all non-zero elements retain their original order,
        and all zeroes are moved to the end with minimal operations.

        Args:
            arr (List[int]): The input list of integers (modified in-place).

        Returns:
            None

        Time Complexity: O(n), where n is the length of the array.
        Space Complexity: O(1), as we are using constant extra space.
        """
        first_ptr = 0  # Position to place the next non-zero element
        n = len(arr)

        # Find the first zero in the array
        while first_ptr < n and arr[first_ptr] != 0:
            first_ptr += 1

        if first_ptr >= n - 1:
            return

        second_ptr = first_ptr + 1

        while second_ptr < n:
            if arr[second_ptr] != 0:
                arr[first_ptr] = arr[second_ptr]
                arr[second_ptr] = 0

                # Move first_ptr to the next zero position
                while first_ptr <= second_ptr and arr[first_ptr] != 0:
                    first_ptr += 1
            second_ptr += 1
