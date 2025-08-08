"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-distinct-elements-in-every-window

Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3.
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.
Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2.
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1.
Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]
Constraints:
1 <= k <= arr.size() <= 105
1 <= arr[i] <= 105
"""


class Solution:
    def countDistinct(self, arr, k):
        """
        ✅ Approach:
        - Use a sliding window of size k and a hashmap (element_tracker) to count the frequency of elements.
        - For each window, store the number of distinct elements at the starting index of the window.
        - After processing all windows, remove the tail of the array to return only the modified portion.

        ⏱️ Time: O(N), but
        ⚠️ Worst-case: Can degrade to O(N*K) if dictionary operations like deletion happen frequently.
        🧠 Space: O(K), for the hashmap storing frequency of elements in the current window
        """

        element_tracker = {}

        # Initialize frequency map with first window
        for i in arr[:k]:
            element_tracker[i] = element_tracker.get(i, 0) + 1

        ptr1 = 0  # Left pointer of the sliding window
        ptr2 = k - 1  # Right pointer of the sliding window

        while True:
            first_element = arr[ptr1]

            # Replace starting index with number of distinct elements
            distinct_elements = len(element_tracker)
            arr[ptr1] = distinct_elements

            # Slide the window: remove the leftmost element from frequency map
            if element_tracker.get(first_element) < 2:
                del element_tracker[first_element]
            else:
                element_tracker[first_element] -= 1

            ptr1 += 1
            ptr2 += 1

            # ! Stop if right pointer exceeds array bounds
            if ptr2 >= len(arr):
                break
            else:
                # Add new incoming element to the window
                next_element = arr[ptr2]
                element_tracker[next_element] = element_tracker.get(next_element, 0) + 1

        # Trim the array to only contain results
        del arr[ptr1:ptr2]
        return arr


"""
# Python program to count distinct elements in every window
# of size k by traversing all windows of size k

from collections import defaultdict

# Function to count distinct elements in every window of size k
def countDistinct(arr, k):
    n = len(arr)  
    res = []
    freq = defaultdict(int)

    # Store the frequency of elements of the first window
    for i in range(k):
        freq[arr[i]] += 1

    # Store the count of distinct elements of the first window
    res.append(len(freq))

    for i in range(k, n):
        freq[arr[i]] += 1
        freq[arr[i - k]] -= 1
    
        # If the frequency of arr[i - k] becomes 0, remove it from the hash map
        if freq[arr[i - k]] == 0:
            del freq[arr[i - k]]
    
        res.append(len(freq))
    
    return res


if __name__=='__main__':
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4

    res = countDistinct(arr, k)
    print(*res)
"""
