"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-subarray-with-given-xor

Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples:

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤105
0 ≤ k ≤ 105
"""


class Solution:
    def subarrayXor(self, arr, k):
        """
        Counts the number of subarrays with XOR equal to k.

        ✅ Approach:
        - Use prefix XOR to reduce the problem to subarray sum with XOR logic.
        - Maintain a hashmap (tracker) of all seen prefix XORs and their frequencies.
        - For each prefix XOR 'xor', we look for 'xor ^ k' in the tracker.
          Why? Because if `prefix1 ^ prefix2 = k`, then `prefix2 = prefix1 ^ k`.

        ⏱️ Time: O(N), where N is the length of the array
        🧠 Space: O(N), due to the hashmap used to store prefix XOR frequencies
        """

        tracker = {0: 1}  # To handle subarrays starting from index 0
        xor = 0  # Running XOR of elements
        ans = 0  # Final count of valid subarrays

        for i in arr:
            # Update prefix XOR
            xor ^= i

            # ? XOR derivation logic:
            #   A ^ B = C
            #   A = C ^ B  (since B ^ B = 0)
            # → So if current prefix XOR is C, and we want A = prefix ^ k,
            #   then we search for (prefix ^ k) in the tracker.
            required = xor ^ k

            # Add the count of such prefix XORs (if any exist)
            if x := tracker.get(required):
                ans += x

            # Update the tracker with current prefix XOR
            tracker[xor] = tracker.get(xor, 0) + 1

        return ans
