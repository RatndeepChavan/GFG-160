"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/k-th-element-of-two-sorted-array1317

Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
Input: a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: Combined sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element of this array is 256.

Constraints:
1 <= a.size(), b.size() <= 106
1 <= k <= a.size() + b.size()
0 <= a[i], b[i] < 108
"""


class Solution:
    def kthElement(self, arr1, arr2, k):
        """
        Finds the K-th smallest element in the union of two sorted arrays.

        Problem:
        Given two sorted arrays arr1 and arr2, and an integer k, return the k-th smallest
        element in the merged sorted array formed by combining both arrays.

        Approach:
        - We perform binary search on the smaller array to partition it and the second array
          such that the total number of elements on the left is equal to k.
        - This allows us to find the k-th element without merging the arrays.
        - We consider edge cases such as out-of-bound indices using -inf/+inf.
        - We aim to maximize the left partition while ensuring all elements on the left are
          less than or equal to elements on the right.

        Time Complexity: O(log(min(len(arr1), len(arr2), k)))
        Space Complexity: O(1)

        Parameters:
        arr1 (List[int]): First sorted array.
        arr2 (List[int]): Second sorted array.
        k (int): The k-th position (1-based index) to find.

        Returns:
        int: The k-th smallest element in the merged sorted array.
        """

        n1, n2 = len(arr1), len(arr2)

        # Ensure arr1 is the smaller array
        if n1 > n2:
            return self.kthElement(arr2, arr1, k)

        low = max(0, k - n2)
        high = min(k, n1)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            l1 = arr1[cut1 - 1] if cut1 > 0 else float("-inf")
            l2 = arr2[cut2 - 1] if cut2 > 0 else float("-inf")

            r1 = arr1[cut1] if cut1 < n1 else float("inf")
            r2 = arr2[cut2] if cut2 < n2 else float("inf")

            # Valid partition found
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)

            # NOTE: Too many elements from arr1, reduce cut1
            elif l1 > r2:
                high = cut1 - 1

            # NOTE: Too few elements from arr1, increase cut1
            else:
                low = cut1 + 1

        return -1  # Should never reach here if input is valid
