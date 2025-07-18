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
        Inserts a new interval into a sorted list of non-overlapping intervals,
        merging if necessary. All operations are performed in-place to maintain
        O(1) auxiliary space.

        Args:
            intervals (List[List[int]]): List of non-overlapping intervals sorted by start time.
            newInterval (List[int]): The new interval to insert [start, end].

        Returns:
            List[List[int]]: Updated list of merged, sorted intervals.

        Time Complexity: O(n) — single pass
        Space Complexity: O(1) — no extra space used
        """
        n = len(intervals)
        new_start, new_end = newInterval

        # Get the overall range of intervals
        first_start = intervals[0][0]
        last_end = intervals[-1][1]

        # ! Case 1: New interval is entirely before all existing intervals
        if new_end < first_start:
            intervals.insert(0, [new_start, new_end])
            return intervals

        # ! Case 2: New interval is entirely after all existing intervals
        if new_start > last_end:
            intervals.append([new_start, new_end])
            return intervals

        # ! Case 3: Only one interval exists — merge directly
        if n == 1:
            start, end = intervals[0]
            intervals[0][0] = min(start, new_start)
            intervals[0][1] = max(end, new_end)
            return intervals

        # * Begin checking overlaps
        swap_idx = None
        for i in range(n):
            cur_start, cur_end = intervals[i]

            # No overlap — current interval ends before new starts
            if cur_end < new_start:
                continue

            # No overlap — current interval starts after new ends
            if cur_start > new_end:
                if swap_idx is None:
                    swap_idx = i
                break

            # Overlap found — mark merge start point
            if swap_idx is None:
                swap_idx = i

            # Expand the new interval to absorb overlapping ranges
            new_start = min(cur_start, new_start)
            new_end = max(cur_end, new_end)

        # * Case 4: Merge all remaining intervals till the end
        if new_end >= intervals[i][1]:
            del intervals[swap_idx:]
            intervals.append([new_start, new_end])
            return intervals

        # * Case 5: Replace overlapping range with merged interval
        intervals[swap_idx:i] = [[new_start, new_end]]
        return intervals
