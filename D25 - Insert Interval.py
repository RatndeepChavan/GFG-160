"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/insert-interval-1666733333

Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.

Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Examples:

Input: intervals = [[1,3], [4,5], [6,7], [8,10]], newInterval = [5,6]
Output: [[1,3], [4,7], [8,10]]
Explanation: The newInterval [5,6] overlaps with [4,5] and [6,7].
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,9]
Output: [[1,2], [3,10], [12,16]]
Explanation: The new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Constraints:
1 ≤ intervals.size() ≤  105
0 ≤ start[i], end[i] ≤ 109
"""


class Solution:
    def insertInterval(self, intervals, newInterval):
        """
        Inserts a new interval into a list of non-overlapping intervals
        sorted by start time, and merges if necessary.

        Time Complexity: O(n) — single pass
        Space Complexity: O(1) — no extra list used beyond the result construction
        """

        n = len(intervals)
        new_start, new_end = newInterval
        swap_idx = None  # First index at which merging should happen

        # ! Special case: only one interval exists
        if n == 1:
            start, end = intervals[0]

            if new_end < start:
                return [[new_start, new_end]] + intervals

            elif new_start > end:
                return intervals + [[new_start, new_end]]

            else:
                # Overlap with the only interval — merge both
                new_start = min(start, new_start)
                new_end = max(end, new_end)
                return [[new_start, new_end]]

        # * General case: iterate over all intervals
        for i in range(n):
            cur_start, cur_end = intervals[i]

            if cur_end < new_start:
                # Current interval ends before new one starts — no overlap
                continue

            if cur_start > new_end:
                # Current interval starts after new one ends — no overlap
                if swap_idx is None:
                    swap_idx = i
                break

            # Overlapping interval detected
            if swap_idx is None:
                swap_idx = i

            # NOTE: Expand the new interval to absorb overlaps
            new_start = min(cur_start, new_start)
            new_end = max(cur_end, new_end)

        # * Insertion logic based on overlap boundaries
        if swap_idx is None and i == 0:
            # Insert new interval before everything — it's the earliest
            return [[new_start, new_end]] + intervals[i:]

        if new_end >= intervals[i][1]:
            # New interval reaches beyond all others — insert and discard rest
            return intervals[:swap_idx] + [[new_start, new_end]]

        # Merge from swap_idx up to i-1 and insert remaining unmerged intervals
        return intervals[:swap_idx] + [[new_start, new_end]] + intervals[i:]
