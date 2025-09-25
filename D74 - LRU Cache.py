"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/linked-list-gfg-160/problem/lru-cache

Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

PUT x y: sets the value of the key x with value y
GET x: gets the value of key x if present else returns -1.
The LRUCache class has two methods get() and put() which are defined as follows.

get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
put(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be initialized.


Examples:

Input: cap = 2, Q = 2, Queries = [["PUT", 1, 2], ["GET", 1]]
Output: [2]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the key-value pair (1, 2) in the cache,
["GET", 1] will print the value corresponding to Key 1, ie 2.

Input: cap = 2, Q = 8, Queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], ["PUT", 1, 2], ["GET", 3]]
Output: [5, -1]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the pair (1,2) in the cache.
["PUT", 2, 3] will insert the pair (2,3) in the cache: 1->2, 2->3(the most recently used one is kept at the rightmost position)
["PUT", 1, 5] will replace the value of 1 from 2 to 5 : 2 -> 3, 1 -> 5
["PUT", 4, 5] : 1 -> 5, 4 -> 5 (Cache size is 2, hence we delete the least recently used key-value pair)
["PUT", 6, 7] : 4 -> 5, 6 -> 7
["GET", 4] : Prints 5 (The cache now looks like 6 -> 7, 4->5)
["PUT", 1, 2] : 4 -> 5, 1 -> 2  (Cache size is 2, hence we delete the least recently used key-value pair)
["GET", 3] : No key value pair having key = 3. Hence, -1 is printed.

Constraints:
1 <= cap <= 103
1 <= Q <= 105
1 <= x, y <= 104
"""


class Node:
    """
    Node structure for doubly linked list used in LRU Cache.

    Attributes:
        key (int): Key of the cache entry.
        val (int): Value of the cache entry.
        prev (Node): Pointer to the previous node in the list.
        next (Node): Pointer to the next node in the list.
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    ✅ Least Recently Used (LRU) Cache

    Uses a combination of:
    - Doubly Linked List: to maintain usage order (most recent at front)
    - Hash Map: to allow O(1) access to nodes

    get(key): O(1)
    put(key, value): O(1)

    ⏱️ Time Complexity: O(1) for both get and put operations.
    🧠 Space Complexity: O(capacity)
    """

    def __init__(self, cap):
        """
        Initializes the LRU Cache with a fixed capacity.

        Args:
            cap (int): Maximum number of elements the cache can hold.
        """
        self.capacity = cap
        self.hashmap = {}

        # Create dummy head and tail nodes to avoid edge checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """
        * Removes a node from the doubly linked list.
        """
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, new_node):
        """
        * Inserts a node right after the head (most recently used position).
        """
        next_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head

        new_node.next = next_node
        next_node.prev = new_node

    def get(self, key):
        """
        ✅ Returns the value of the key if present, else -1.
        * Also moves the accessed node to the front (MRU position).

        Args:
            key (int): The key to retrieve.

        Returns:
            int: The value associated with the key, or -1 if not found.
        """
        if key in self.hashmap:
            map_node = self.hashmap[key]

            # Move to front (MRU)
            self._remove(map_node)
            self._insert(map_node)

            return map_node.val

        return -1

    def put(self, key, value):
        """
        ✅ Adds a key-value pair to the cache.
        * If key exists, updates value and moves to front.
        * If capacity exceeded, evicts the LRU node.

        Args:
            key (int): The key to add or update.
            value (int): The value associated with the key.
        """
        if key in self.hashmap:
            # Remove the old node
            self._remove(self.hashmap[key])

        # Insert the new node at front
        new_node = Node(key, value)
        self.hashmap[key] = new_node
        self._insert(new_node)

        # Evict LRU if needed
        if len(self.hashmap) > self.capacity:
            last_node = self.tail.prev  # Least recently used node (just before tail)
            self._remove(last_node)
            del self.hashmap[last_node.key]
