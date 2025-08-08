"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/product-array-puzzle4525


Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.

Examples:

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: For i = 0, res[i] is 0.
For i = 1, res[i] is 12.

Constraints:
2 <= arr.size() <= 105
-100 <= arr[i] <= 100
"""


class Solution:
    def productExceptSelf(self, arr):
        """
        ✅ Approach:
            - First pass: Count zeros and calculate product of non-zero elements.
            - If more than 1 zero: All products will be zero.
            - If exactly 1 zero: Only the zero's position will have the product of non-zero elements.
            - Else: For each index, result[i] = total_product // arr[i]

        ⏱️ Time Complexity: O(n)
            - One pass to compute product and zeros
            - One pass to construct the result

        🧠 Space Complexity: O(n)
            - Result list of size n

        ! Note:
            - No division-by-zero risk due to handling zeros explicitly
            - Integer division (`//`) used for integer array inputs

        Args:
            arr (List[int]): Input array of integers

        Returns:
            List[int]: Product of all elements except self at each index
        """
        zeros_found = 0
        total_product = 1

        for num in arr:
            if num == 0:
                zeros_found += 1
            else:
                total_product *= num

            # ? More than one zero means all products will be zero
            if zeros_found > 1:
                return [0] * len(arr)

        res = []
        for num in arr:
            if num == 0:
                # ✅ Only one zero, this index gets product
                res.append(total_product)
            else:
                if zeros_found == 1:
                    res.append(0)  # ✅ All other indices get 0
                else:
                    res.append(total_product // num)  # ✅ Normal division

        return res
