"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/kth-missing-positive-number-in-a-sorted-array


Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].

Examples :

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.
Input: arr[] = [1, 2, 3], k = 2
Output: 5
Explanation: Missing are 4, 5, 6… and 2nd missing number is 5.
Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
Output: 2
Explanation: Missing are 1, 2, 4, 6… and 2nd missing number is 2.

Constraints:
1 <= arr.size() <= 105
1 <= k <= 105
1 <= arr[i]<= 106
"""


class Solution:
    def kthMissing(self, arr, k):
        """
        Function to find the k-th missing positive number in a sorted array.

        Approach:
        - We are given a sorted array of positive integers.
        - We calculate the number of missing elements until a certain index using:
            missing = arr[index] - (index + 1)
          This works because the expected value at index `i` in a perfect array without missing numbers is `i + 1`.

        - Perform binary search to find the point where total missing becomes ≥ k,
          and use this to calculate the exact k-th missing number.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        n = len(arr)
        low = 0
        high = n - 1

        # ! Check if the k-th missing number lies before the first element
        initially_missing = arr[low] - 1
        if k <= initially_missing:
            return k

        # ! Check if the k-th missing number lies beyond the last element
        total_missing = arr[high] - n
        if k > total_missing:
            return arr[high] + (k - total_missing)

        # Binary search to find the first index where missing count ≥ k
        while low <= high:
            mid = (low + high) // 2

            # Number of missing elements till index mid
            valid_value = mid + 1
            cur_missing_numbers = arr[mid] - valid_value

            if cur_missing_numbers < k:
                low = mid + 1
                nxt_missing_numbers = arr[low] - (low + 1)
                # NOTE : IndexError for low+1 won't occur as we handled that as second edge

                if nxt_missing_numbers >= k:
                    return arr[mid] + (k - cur_missing_numbers)
            else:
                high = mid - 1


# ! SHORTER VERSION


class Solution:
    def kthMissing(arr, k):
        lo = 0
        hi = len(arr) - 1
        res = len(arr) + k

        # Binary Search for index where arr[i] > (i + k)
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] > mid + k:
                res = mid + k
                hi = mid - 1
            else:
                lo = mid + 1

        return res
