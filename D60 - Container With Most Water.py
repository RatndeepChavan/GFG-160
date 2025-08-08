"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/container-with-most-water0535

Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Note: In the case of a single vertical line it will not be able to hold water.

Examples:

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base is 2. Height of container = min(5, 3) = 3. So, total area to hold water = 3 * 2 = 6.
Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are 4 distance apart. So the size of the base is 4. Height of container = min(5, 3) = 3. So, total area to hold water = 4 * 3 = 12.
Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
Explanation: 8 and 5 are 5 distance apart. So the size of the base is 5. Height of container = min(8, 5) = 5. So, the total area to hold water = 5 * 5 = 25.

Constraints:
1<= arr.size() <=105
1<= arr[i] <=104
"""


class Solution:
    def maxWater(self, arr):
        """
        Calculates the maximum water that can be trapped between two vertical lines.

        ✅ Approach:
            - Two-pointer technique:
              Start with the widest container (left at 0, right at n-1) and narrow it down.
            - At each step, compute the area between left and right lines using:
                area = (right - left) * min(arr[left], arr[right])
            - Move the pointer pointing to the shorter line inward, because that limits the height.
              This ensures we explore the potential for a higher minimum height.

        ! A single vertical line or empty input can't hold any water.

        ⏱️ Time Complexity: O(n)
            - Each element is visited at most once (either left++ or right--).

        🧠 Space Complexity: O(1)
            - No extra space is used, only pointers and a few variables.

        Args:
            arr (List[int]): List of non-negative integers representing line heights.

        Returns:
            int: Maximum area of water that can be contained.
        """

        n = len(arr)

        # ! At least two lines needed to form a container
        if n < 2:
            return 0

        left = 0
        right = n - 1
        max_water = 0

        while left < right:
            width = right - left
            height = min(arr[left], arr[right])
            current_water = width * height
            max_water = max(max_water, current_water)

            # ? Move the pointer pointing to the shorter line
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_water
