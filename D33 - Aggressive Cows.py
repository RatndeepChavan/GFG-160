"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/aggressive-cows

You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[2] and
the third cow can be placed at stalls[3].
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.
Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.

Constraints:
2 <= stalls.size() <= 106
0 <= stalls[i] <= 108
2 <= k <= stalls.size()
"""


class Solution:

    @staticmethod
    def check_allocation(arr, dist, cows):
        """
        Helper function to check if cows can be placed in stalls
        with at least `dist` distance apart.

        Parameters:
        arr (List[int]) : Sorted stall positions
        dist (int) : Minimum distance to maintain between cows
        cows (int) : Number of cows to place

        Returns:
        bool : True if placement is possible, else False
        """
        prev_allocation = arr[0]
        allocated_cows = 1

        for i in range(1, len(arr)):
            if arr[i] - prev_allocation >= dist:
                allocated_cows += 1
                prev_allocation = arr[i]

                # If all cows are placed successfully
                if allocated_cows >= cows:
                    return True

        return False

    def aggressiveCows(self, stalls, k):
        """
        Main function to find the largest minimum distance between cows
        placed in stalls such that they are as aggressive (far apart) as possible.

        Approach:
        - Sort the stalls.
        - Use binary search to find the largest distance that satisfies the condition.
        - Use a helper function to validate a distance.

        Time Complexity:
        - O(n log(max_dist)) where:
            - n is the number of stalls
            - max_dist = stalls[-1] - stalls[0] (after sorting)
        Space Complexity: O(1)

        Why we ignore sorting complexity O(n log n):
        - Although sorting is required, the difference `max_dist = max(stalls) - min(stalls)` tends to dominate `n` in most practical or competitive scenarios.
        - For unique and sparse stall positions (e.g., [1, 100, 1000, 10000]), `log(max_dist) >> log(n)`
        - Therefore, binary search + greedy dominates the overall complexity.

        Parameters:
        stalls (List[int]) : Unsorted list of stall positions
        k (int) : Number of cows to place

        Returns:
        int : Largest minimum distance possible between cows
        """
        stalls.sort()

        # ! NOTE: We start from low = 2 since all stalls are unique and sorted,
        # ! so the minimum difference must be at least 1.
        # ! We initialize distance = 1 as the fallback.
        distance = 1
        low = 2  # generally initiated as low = 1
        high = stalls[-1] - stalls[0]

        while low <= high:
            mid = (low + high) // 2

            if self.check_allocation(stalls, mid, k):
                distance = max(distance, mid)
                low = mid + 1  # Try for larger distance
            else:
                high = mid - 1  # Reduce the distance

        return distance
