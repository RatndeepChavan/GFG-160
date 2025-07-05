"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/non-overlapping-intervals

Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.
Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: You need to remove two [1, 3] to make the rest of the intervals non-overlapping.
Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non overlapping.

Constraints:
1 ≤ intervals.size() ≤  105
|intervalsi| == 2
0 ≤ starti < endi <=5*104
"""


class Solution:
    def minRemoval(self, intervals):
        """
        Returns the minimum number of intervals to remove to make the rest non-overlapping.

        Time Complexity: O(n log n) — due to sorting
        Space Complexity: O(1) — in-place comparison, no extra storage
        """

        # * Step 1: Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        count = 0  # Number of intervals to remove
        prev_end = intervals[0][1]  # End of the last non-overlapping interval

        # * Step 2: Iterate through the rest of the intervals
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]

            if prev_end > cur_start:
                # Overlap detected — need to remove one interval
                count += 1

                # ? We keep the interval with the smaller end time to minimize future overlaps.
                # This greedy choice helps preserve as many non-overlapping intervals as possible.
                prev_end = min(prev_end, cur_end)
            else:
                # No overlap — move to the next interval
                prev_end = cur_end

        return count
