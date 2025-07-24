"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-possible-triangles-1587115620

Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Examples:

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.
Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]
Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.

Constraints:
1 ≤ arr.size() ≤ 103
0 ≤ arr[i] ≤ 105
"""


class Solution:
    def countTriangles(self, arr):
        """
        Counts the number of triplets (i, j, k) that can form a valid triangle.

        ✅ Approach:
        - Sort the array to apply two-pointer logic efficiently.
        - Fix the largest side (starting from the end).
        - Use two pointers from the start and just before the fixed side to find valid pairs.
        - If arr[left] + arr[right] > arr[i], then all elements between left and right form valid triangles.

        ⏱️ Time: O(N^2), N = length of array
        🧠 Space: O(1), no extra space used beyond variables
        """

        arr.sort()
        n = len(arr)
        triangles_found = 0

        # * Iterate backwards fixing the largest side of the triangle
        for i in range(n - 1, 1, -1):
            biggest_side = arr[i]
            left = 0
            right = i - 1

            # * Use two-pointer approach to find valid (left, right) pairs
            while left < right:
                other_sides_sum = arr[left] + arr[right]

                # If valid triangle condition satisfied
                if other_sides_sum > biggest_side:
                    triangles_found += right - left
                    # Move right to check for more pairs
                    right -= 1
                else:
                    # Move left forward if condition not satisfied
                    left += 1

        return triangles_found
