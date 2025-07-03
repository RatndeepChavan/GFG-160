"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620

Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].
Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1]
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.

Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
"""

from typing import List


def circularSubarraySum(arr: List[int]) -> int:
    """
    Finds the maximum possible sum of a circular subarray.

    There are two cases:
    1. The max subarray is non-circular → use Kadane's algorithm
    2. The max subarray wraps around the end → use:
       total sum - minimum subarray sum

    To handle the edge case when all elements are negative,
    we fall back to standard Kadane's result.

    Args:
        arr (List[int]): The input array.

    Returns:
        int: Maximum circular subarray sum.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    total_sum = 0
    current_max = current_min = 0
    max_sum = float("-inf")
    min_sum = float("inf")

    for num in arr:
        total_sum += num

        # Max subarray sum (Kadane's)
        current_max = max(current_max + num, num)
        max_sum = max(max_sum, current_max)

        # Min subarray sum (for circular wrap)
        current_min = min(current_min + num, num)
        min_sum = min(min_sum, current_min)

    # If all elements are negative, total_sum == min_sum
    if total_sum == min_sum:
        return max_sum

    return max(max_sum, total_sum - min_sum)
