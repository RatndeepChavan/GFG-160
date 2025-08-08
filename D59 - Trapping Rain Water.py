"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/trapping-rain-water-1587115621


Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
|
|                               | block |
| block | WATER | WATER | WATER | block |
| block | WATER | WATER | WATER | block | WATER | block |
| block | WATER | block | WATER | block | WATER | block |
---------------------------------------------------------
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.
Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.
Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.
Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.

Constraints:
1 < arr.size() < 105
0 < arr[i] < 103
"""

"""
Approach in Plain English:

We first get the left and right walls, then assume the space between them is empty.
We calculate the water using the smaller of the two wall heights (as water can't exceed the shorter wall).

As we start iterating inward, if a wall is shorter than current wall height, we just subtract its height from total water (since it displaces water).

But when we find a wall taller than our current wall height, we know more water can be stored!
So we:

Remove previously stored water based on wall_height,

Based on max_height and current wall height, calculate increased height,

Add the extra water stored due to this increase, assuming all in-between walls are zero.

💡 Importantly, we only calculate water for increased height because previous height was already used when we did wall_height * (right - left - 1).
"""


class Solution:
    def maxWater(self, arr):
        """
        ✅ Approach:
        - Start from the leftmost and rightmost non-zero-height bars.
        - Set the initial water level as the shorter of the two boundary bars.
        - Move inward, updating water trapped at each step:
            -> If current bar height is less than wall height → it traps water.
            -> If current bar height is equal or greater → update wall height.
        - Adjust water count accordingly to avoid over-counting.


        ⏱️ Time: O(N)
        🧠 Space: O(1)
        """

        n = len(arr)

        # ! Not enough walls to trap any water
        if n < 3:
            return 0

        # * Step 1: Find the first valid wall from the left
        left = 0
        while arr[left] < 1:
            left += 1

        # * Step 2: Find the first valid wall from the right
        right = n - 1
        while arr[right] < 1:
            right -= 1

        # * Step 3: Assuming empty space between two walls calculate stored water
        max_height = max(arr[left], arr[right])  # Highest wall
        wall_height = min(arr[left], arr[right])  # Wall that defines water level

        # ? Why (right - left - 1)?
        # - We only store water **between** the two walls.
        # - So, exclude both boundary walls → right - left - 1
        water_stored = wall_height * (right - left - 1)

        # * Step 4: Move inward, one wall at a time
        while True:
            if arr[left] < arr[right]:
                left += 1
                wall_idx = left
            else:
                right -= 1
                wall_idx = right

            if left >= right:
                break

            current_height = arr[wall_idx]

            # * Shorter wall so just remove stored water equal to height
            if current_height < wall_height:
                water_stored -= current_height

            # * Taller/same height wall found
            else:
                # ? We previously assumed water stored till wall_height level
                #   So remove that assumption for current index
                water_stored -= wall_height

                # ? Increased height logic explained:
                # - We only want to add water for the **newly increased height**
                #   because water for wall_height (previous height) was counted earlier.

                # * Wall is taller than max_height : update wall_height and max_height
                if current_height > max_height:
                    # ? as current wall is taller than max height so water will be filled till max_height
                    increased_height = max_height - wall_height
                    wall_height = max_height
                    max_height = current_height

                # * Wall is in between wall_height and max_height : update wall_height
                else:
                    # ? as current wall is shorter than max height so water will be filled till current wall
                    increased_height = current_height - wall_height
                    wall_height = current_height

                # * Add extra water volume due to increased height
                # ? This assumes all walls between left and right are 0-height
                water_stored += (right - left - 1) * increased_height

        return water_stored


A = [3, 0, 1, 0, 4, 0, 2]
A = [3, 0, 2, 0, 4]
A = [1, 2, 3, 4]
A = [1, 2, 3, 4, 1, 3, 2]
ans = Solution().maxWater(A)
print(ans)
# 3 0 1 0 4 0 2 / 10
# 3 0 2 0 4 / 7
# 1 2 3 4 / 0
# 1 2 3 4 1 3 2 / 2


"""
! ALTERNATIVE MOST KNOWN Lmax AND Rmax APPROACH

def maxWater(arr):
    left = 1
    right = len(arr) - 2

    # lMax : Maximum in subarray arr[0..left-1]
    # rMax : Maximum in subarray arr[right+1..n-1]
    lMax = arr[left - 1]
    rMax = arr[right + 1]

    res = 0
    while left <= right:
        # If rMax is smaller, then we can decide the 
        # amount of water for arr[right]
        if rMax <= lMax:
            # Add the water for arr[right]
            res += max(0, rMax - arr[right])

            # Update right max
            rMax = max(rMax, arr[right])

            # Update right pointer as we have decided 
            # the amount of water for this
            right -= 1
        else: 
            # Add the water for arr[left]
            res += max(0, lMax - arr[left])

            # Update left max
            lMax = max(lMax, arr[left])

            # Update left pointer as we have decided 
            # the amount of water for this
            left += 1
    return res

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(maxWater(arr))
"""
