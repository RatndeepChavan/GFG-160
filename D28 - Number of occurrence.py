"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/number-of-occurrence2259

Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[].

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106
"""


class Solution:
    first = -1
    last = -1

    def find_target(self, arr, target, low, high):
        """
        Recursive binary search to find both first and last occurrence of the target.
        Updates class variables: `first` and `last`.

        Time Complexity:
            - Best/Average Case: O(log n)
            - Worst Case: O(n) if all elements equal target and both sides are fully explored.
            ? However, we avoid this worst case via an early check in countFreq().

        Space Complexity:
            - Best/Average Case: O(log n) due to recursion stack
            - Worst Case: O(n) if all recursive branches are taken
            ? But since we don't create subarrays and arr is passed by reference, there's no memory duplication.
        """
        if low > high:
            return

        mid = (low + high) // 2

        if arr[mid] > target:
            self.find_target(arr, target, low, mid - 1)
        elif arr[mid] < target:
            self.find_target(arr, target, mid + 1, high)
        else:
            # ? Update first and last if better index found
            if self.first == -1 or mid < self.first:
                self.first = mid
            if self.last == -1 or mid > self.last:
                self.last = mid

            # ? Continue to search both halves for more target occurrences
            self.find_target(arr, target, low, mid - 1)
            self.find_target(arr, target, mid + 1, high)

    def countFreq(self, arr, target):
        """
        Counts frequency of target in a sorted array.

        Args:
            arr (List[int]): Sorted input array
            target (int): Target number to count

        Returns:
            int: Frequency of target in arr

        NOTE: We reset the class-level first/last indices before every run.

        ? Early return optimization handles uniform arrays in O(1)
        """
        # Reset state
        self.first = -1
        self.last = -1

        # ? Short-circuit when all elements are greater or lesser than target
        if target < arr[0] or target > arr[-1]:
            return 0

        # ? Short-circuit worst case when all elements = target
        if target == arr[0] and target == arr[-1]:
            return len(arr)

        self.find_target(arr, target, 0, len(arr) - 1)

        return (self.last - self.first + 1) if self.first != -1 else 0


"""
# ! SIMPLE SOLUTION USING PYTHON BISECT MODULE

# Python program to count occurrence of a given target
# using binary search

from bisect import bisect_left, bisect_right

# Function to find the occurrence of the given target 
# using binary search
def countFreq(arr, target):
    l = bisect_left(arr, target)
    r = bisect_right(arr, target)
    
    # Return the difference between upper bound and 
    # lower bound of the target
    return r - l

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 2
    print(countFreq(arr, target))
"""
