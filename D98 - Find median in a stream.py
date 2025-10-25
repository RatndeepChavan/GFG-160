"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/heap-gfg-160/problem/find-median-in-a-stream-1587115620

Given a data stream arr[] where integers are read sequentially, the task is to determine the median of the elements encountered so far after each new integer is read.

There are two cases for median on the basis of data set size.

1. If the data set has an odd number then the middle one will be consider as median.
2. If the data set has an even number then there is no distinct middle value and the median will be the arithmetic mean of the two middle values.

Examples:

Input:  arr[] = [5, 15, 1, 3, 2, 8]
Output: [5.0, 10.0, 5.0, 4.0, 3.0, 4.0] 
Explanation: 
After reading 1st element of stream - 5 -> median = 5.0
After reading 2nd element of stream - 5, 15 -> median = (5+15)/2 = 10.0 
After reading 3rd element of stream - 5, 15, 1 -> median = 5.0
After reading 4th element of stream - 5, 15, 1, 3 ->  median = (3+5)/2 = 4.0
After reading 5th element of stream - 5, 15, 1, 3, 2 -> median = 3.0
After reading 6th element of stream - 5, 15, 1, 3, 2, 8 ->  median = (3+5)/2 = 4.0

Input: arr[] = [2, 2, 2, 2]
Output: [2.0, 2.0, 2.0, 2.0]
Explanation: 
After reading 1st element of stream - 2 -> median = 2.0
After reading 2nd element of stream - 2, 2 -> median = (2+2)/2 = 2.0
After reading 3rd element of stream - 2, 2, 2 -> median = 2.0
After reading 4th element of stream - 2, 2, 2, 2 ->  median = (2+2)/2 = 2.0

Constraints:
1 <= arr.size() <= 105
1 <= x <= 106
"""

import heapq
import bisect

# ------------------------------------------------------------------
# * 🔵 1. Two Heaps Approach (Efficient)
# ------------------------------------------------------------------
class MedianFinderHeaps:
    """
    🧩 Approach:
    ------------
    - Maintain two heaps:
        1. `small` → Max-Heap (using negatives) for the smaller half.
        2. `large` → Min-Heap for the larger half.
    - Keep heaps balanced (size difference ≤ 1).
    - Median:
        - If sizes equal → average of tops
        - Else → top of the heap with extra element

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(log n)** per insertion (heap push/pop)
    - 🧠 **Space: O(n)** (store all numbers in heaps)

    ✅ Standard approach for real-time median queries.
    """

    def __init__(self):
        self.small = []  # Max-heap (as negatives)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        """Insert a number into the two-heaps structure."""
        s_len, l_len = len(self.small), len(self.large)

        # Get current tops (inf/-inf if empty)
        s_top = -self.small[0] if s_len else float("inf")
        l_top = self.large[0] if l_len else float("-inf")

        # * Case 1: small has more → push to large
        if s_len > l_len:
            if num < s_top:
                # ? why use heappushpop here?
                # Because we want to insert num into small, but small already has extra element.
                # Instead of pushing and then popping (two ops), we do push+pop in one.
                # The popped value (largest of small) is the correct candidate for large.
                num = -1 * heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, num)

        # * Case 2: large has more → push to small
        elif s_len < l_len:
            if num > l_top:
                # ? why use heappushpop here?
                # Same logic: insert num into large, pop its smallest.
                # The popped value is smaller than num → belongs in small.
                num = heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, -num)

        # * Case 3: equal size → push based on value
        else:
            if num > s_top:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -num)

    def getMedian(self, arr):
        """Insert numbers one by one and return running medians."""
        res = []
        for num in arr:
            self.addNum(num)
            if len(self.small) > len(self.large):
                res.append(-self.small[0])                          # top of max-heap
            elif len(self.small) < len(self.large):
                res.append(self.large[0])                           # top of min-heap
            else:
                res.append((-self.small[0] + self.large[0]) / 2)    # average
        return res


# ------------------------------------------------------------------
# * 🟡 2. Naive Approach (Sorted Array + Bisect)
# ------------------------------------------------------------------
class MedianFinderNaive:
    """
    🧩 Approach:
    ------------
    - Keep all numbers in a sorted list.
    - Insert each number at the correct position (using `bisect.insort`).
    - Median is simply middle element(s).

    📊 Complexity:
    --------------
    - ⏱️ **Time: O(n)** per insertion (list insertion is costly)
    - 🧠 **Space: O(n)** large streams (O(n²) overall

    ✅ Easy to understand and implement.
    ❌ Not efficient for large streams (O(n²) overall).
    """

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        """Insert number into sorted list."""
        bisect.insort(self.data, num)

    def getMedian(self, arr):
        """Insert numbers one by one and return running medians."""
        res = []
        for num in arr:
            self.addNum(num)
            n = len(self.data)
            
            # Odd
            if n % 2 == 1:  
                res.append(self.data[n // 2])
            
            # Even
            else:           
                res.append((self.data[(n // 2) - 1] + self.data[n // 2]) / 2)
        return res
