"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/heap-gfg-160/problem/k-closest-points-to-origin--172242

Given an array of points where each point is represented as points[i] = [xi, yi] on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance, defined as: 

sqrt( (x2 - x1)2 + (y2 - y1)2 )

Note: You can return the k closest points in any order, driver code will sort them before printing.

Examples:
Input: k = 2, points[] = [[1, 3], [-2, 2], [5, 8], [0, 1]]
Output: [[-2, 2], [0, 1]]
Explanation: The Euclidean distances from the origin are:
Point (1, 3) = sqrt(10)
Point (-2, 2) = sqrt(8)
Point (5, 8) = sqrt(89)
Point (0, 1) = sqrt(1)
The two closest points to the origin are [-2, 2] and [0, 1].

Input: k = 1, points = [[2, 4], [-1, -1], [0, 0]]
Output: [[0, 0]]
Explanation: The Euclidean distances from the origin are:
Point (2, 4) = sqrt(20)
Point (-1, -1) = sqrt(2)
Point (0, 0) = sqrt(0)
The closest point to origin is (0, 0).

Constraints:
1 <= k <= points.size() <= 105
-104 <= xi, yi <= 104
"""


from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        🧩 Optimization: 
        Since sqrt() is monotonic, we can skip it and just use (x² + y²).

        ⚙️ Approach (Min-Heap):
        -----------------------
        1️⃣ Compute distance for each point.  
        2️⃣ Push tuple (distance, x, y) into a min-heap.  
        3️⃣ Pop `k` times from the heap → get the closest `k` points.  

        📊 Complexity:
        --------------
        - Heapify → O(n)  
        - Extract k → O(k log n)  
        - Total → O(n + k log n)  
        - Space → O(n) (heap stores all points)

        🎯 Why Heap?
        ------------
        - Min-heap ensures smallest distances always pop first.  
        - Clean and intuitive to implement.  
        """

        minHeap = []

        # * Step 1: Build array of (distance, x, y)
        for x, y in points:
            dist = (x ** 2) + (y ** 2)   # no sqrt needed
            minHeap.append([dist, x, y])

        # * Step 2: Turn into heap in O(n)
        heapq.heapify(minHeap)

        # * Step 3: Extract k closest points
        res = []
        while k:
            # always smallest distance
            dist, x, y = heapq.heappop(minHeap)  
            res.append([x, y])
            k -= 1

        return res


# ------------------------------------------------------------------
# 🔹 Alternative: Max-Heap of size k
# ------------------------------------------------------------------

class SolutionOptimized:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        ⚡ Optimized Approach (Max-Heap of size k)
        ------------------------------------------
        Idea:
        - Keep only k closest points seen so far.
        - Use max-heap (store -distance).
        - If new point is closer than current farthest → replace it.

        📊 Complexity:
        --------------
        - Each push/pop → O(log k)  
        - For n points → O(n log k)  
        - Space → O(k), smaller than full min-heap.
        """

        maxHeap = []

        # * Step 1: Process all points
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            # store negative for max-heap
            heapq.heappush(maxHeap, (-dist, x, y))  

            # * Step 2: Keep heap size ≤ k
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # * Step 3: Extract k closest
        return [[x, y] for (_, x, y) in maxHeap]