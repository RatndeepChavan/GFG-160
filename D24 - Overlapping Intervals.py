"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/overlapping-intervals--170633

Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, [1,3] and [2,4] which on merging will become [1,4]. Therefore we will return [[1,4], [6,8], [9,10]].
Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: In the given intervals all the intervals overlap with the interval [1,9]. Therefore we will return [1,9].

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ starti ≤ endi ≤ 105
"""


class Solution:
    def mergeOverlap(self, arr):
        """
        Merges all overlapping intervals in-place.

        Time Complexity: O(n log n) — for sorting
        Space Complexity: O(1) — in-place merging using overwrite
        """

        # * Sort intervals based on starting time
        arr.sort()

        i = 0  # Points to the last merged interval
        j = 1  # Pointer scanning the current interval

        while j < len(arr):
            prev_start, prev_end = arr[i]
            cur_start, cur_end = arr[j]

            if cur_start <= prev_end:
                # * Overlap case: merge intervals by extending the end
                arr[i][1] = max(prev_end, cur_end)
                j += 1
            else:
                i += 1

                # * No overlap — move this non-overlapping interval forward
                arr[i][0] = arr[j][0]
                arr[i][1] = arr[j][1]
                j += 1

                # NOTE: We're overwriting arr[i] with arr[j] intentionally.
                # This ensures all valid merged intervals are packed at the front.
                # It avoids creating a new list, keeping space complexity O(1).

        # * Final merged intervals lie in arr[0] to arr[i] inclusive
        # NOTE: We return arr[:i + 1] because i is the index of the last valid merged interval.
        # Since slicing is non-inclusive at the end, we use i + 1.
        return arr[: i + 1]
