"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/pair-in-array-whose-sum-is-closest-to-x1124

Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:
Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.
Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target.
Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.

Constraints:
1 <= arr.size() <= 2*105
0 <= target<= 2*105
0 <= arr[i] <= 105
"""


class Solution:
    def sumClosest(self, arr, target):
        """
        Finds two elements in the array whose sum is closest to the given target.

        ✅ Approach:
        - Sort the array to apply two-pointer technique.
        - Use two pointers (start, end) to explore potential sums.
        - Track the closest sum difference (`dist`) and the associated pair (`ans`).
        - Update the result when a better (closer) sum is found.

        ⏱️ Time: O(N log N) due to sorting
        🧠 Space: O(1)
        """

        n = len(arr)

        # ! Edge case: If only one element, we cannot form a pair
        if n < 2:
            return []

        # * Sorting for two-pointer application
        arr.sort()

        dist = float("inf")  # Smallest distance from target seen so far
        ans = [arr[0], arr[-1]]  # Initial pair

        start = 0
        end = n - 1

        while start < end:
            addition = arr[start] + arr[end]
            current_dist = abs(target - addition)

            # * Update closest pair if distance improves
            if current_dist < dist:
                ans = [arr[start], arr[end]]
                dist = current_dist

            if addition > target:
                # Move end pointer to reduce sum
                end -= 1
            elif addition < target:
                # Move start pointer to increase sum
                start += 1
            else:
                # Exact match found
                break

        return ans
