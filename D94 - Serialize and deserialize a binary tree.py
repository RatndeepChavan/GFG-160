"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/tree-gfg-160/video/MzA1NTY%3D

Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the level order traversal of the tree returned by deSerialize(serialize(input_tree)).

Examples :

Input: root = [1, 2, 3]       

Output: [1, 2, 3]
Input: root = [10, 20, 30, 40, 60, N, N] 

Output: [10, 20, 30, 40, 60]
Constraints:
1 ≤ Number of nodes ≤ 104
1 ≤ Data of a node ≤ 109
"""
# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class SolutionCustom:
    """
    ✅ Custom Serialization Approach (Out-of-the-box idea)
    
    Uniqueness:
    -----------
    Instead of storing explicit `None` for missing children (like standard BFS/DFS methods),
    each node is represented as a string where:
        - "N" prefix  → left child is missing
        - "N" suffix  → right child is missing
        - Example: "N5N" means a node with value 5 and no children (leaf).
            "N7"  means value 7 with no left child but has right child.
            "9N"  means value 9 with left child but no right child.
    
    Advantages:
    -----------
    - Leaf nodes are directly visible (`"NvalueN"`).
    - Skew direction (left vs right heavy) can be inferred from prefixes/suffixes.
    - Saves space in skewed trees (fewer `None` markers compared to BFS).
    - Passed all GFG test cases successfully.
    
    Approach:
    ---------
    - Serialize: Do a BFS traversal. For each node:
        * Encode its value with "N" if left/right child is missing.
        * Append this string to array.
    - Deserialize: Reverse the process.
        * For each encoded node string, decide whether left/right child exists.
        * Rebuild tree level by level.
    """

    def serialize(self, root):
        """Serialize tree into custom array representation."""
        if not root:
            return []

        tree_arr = []
        queue = [root]
        while queue:
            width = len(queue)
            for _ in range(width):
                current = queue.pop(0)
                current_str = str(current.data)

                # If left child missing → mark prefix "N"
                if current.left:
                    queue.append(current.left)
                else:
                    current_str = "N" + current_str

                # If right child missing → mark suffix "N"
                if current.right:
                    queue.append(current.right)
                else:
                    current_str += "N"

                tree_arr.append(current_str)
        return tree_arr

    def deSerialize(self, arr):
        """Deserialize custom array back into tree."""
        if not arr:
            return None

        # Helper: strip markers to get node value
        def get_value(val):
            if val[0] == "N":
                val = val[1:]
            if val[-1] == "N":
                val = val[:-1]
            return int(val)

        val = get_value(arr[0])
        root = Node(val)
        queue = [root]
        ptr = 1

        for node_str in arr:
            current = queue.pop(0)

            # Left child exists?
            if node_str[0] == "N":
                current.left = None
            else:
                val = get_value(arr[ptr])
                ptr += 1
                node = Node(val)
                queue.append(node)
                current.left = node

            # Right child exists?
            if node_str[-1] == "N":
                current.right = None
            else:
                val = get_value(arr[ptr])
                ptr += 1
                node = Node(val)
                queue.append(node)
                current.right = node

        return root


# ------------------------------------------------------------------
# 🔹 Standard Solutions (for completeness and reference)
# ------------------------------------------------------------------

class SolutionBFS:
    """
    ✅ Standard BFS-based Serialization (Level Order with 'None' markers)
    
    Approach:
    ---------
    - Serialize:
        * Do level-order traversal.
        * Store node values; if a child is missing, store None.
    - Deserialize:
        * Rebuild tree level by level using stored values.
    
    - Time:  O(N)   | N = number of nodes
    - Space: O(N)   | stores explicit None markers
    """

    def serialize(self, root):
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.data)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        return result

    def deSerialize(self, arr):
        if not arr or arr[0] is None:
            return None

        root = Node(arr[0])
        queue = [root]
        i = 1
        while queue and i < len(arr):
            current = queue.pop(0)
            if arr[i] is not None:
                current.left = Node(arr[i])
                queue.append(current.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                current.right = Node(arr[i])
                queue.append(current.right)
            i += 1
        return root


class SolutionDFS:
    """
    ✅ Standard DFS-based Serialization (Preorder with 'None' markers)
    
    Approach:
    ---------
    - Serialize:
        * Use preorder traversal.
        * If node exists → append value.
        * If node missing → append None.
    - Deserialize:
        * Rebuild tree recursively by consuming values in preorder order.
    
    - Time:  O(N)
    - Space: O(H) recursion stack, H = tree height
    """

    def serialize(self, root):
        result = []

        def preorder(node):
            if not node:
                result.append(None)
                return
            result.append(node.data)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result

    def deSerialize(self, arr):
        self.index = 0

        def build():
            if self.index >= len(arr) or arr[self.index] is None:
                self.index += 1
                return None
            node = Node(arr[self.index])
            self.index += 1
            node.left = build()
            node.right = build()
            return node

        return build()


# ----------------------------------------------------------------------
# * 🌳 Example Trees and Their Representations
# ----------------------------------------------------------------------

"""
1. Balanced Tree (3 levels)
        1
       / \
      2   3
     / \ / \
    4  5 6  7

Custom:   ['1', '2', '3', '45', '67']
BFS:      [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]
DFS:      [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]


2. Left Skewed Tree (5 levels)
        1
       /
      2
     /
    3
   /
  4
 /
5

Custom:   ['N1', 'N2', 'N3', 'N4', 'N5N']
BFS:      [1, 2, None, 3, None, 4, None, 5, None, None]
DFS:      [1, 2, 3, 4, 5, None, None, None, None, None, None]


3. Right Skewed Tree (5 levels)
    1
     \
      2
       \
        3
         \
          4
           \
            5

Custom:   ['N1', 'N2', 'N3', 'N4', 'N5N']
BFS:      [1, None, 2, None, 3, None, 4, None, 5, None]
DFS:      [1, None, 2, None, 3, None, 4, None, 5, None, None]
"""


"""
🚀 Tree Serialization — With a Twist!

Today I explored the classic *tree serialization & deserialization* problem, but instead of going with the usual BFS/DFS approaches, I tried something a little different.

💡 What's Different?
Each node is encoded as a string with `"N"` markers
   • `"N5N"` → value `5`, no children (leaf)
   • `"N7"` → value `7`, no left child but has right child
   • `"9N"` → value `9`, has left child but no right child

🌟 Advantages Over Standard Methods
✅ Space-efficient for skewed trees (fewer None markers)
✅ Makes tree structure patterns easy to visualize
✅ Leaf nodes are easy to spot directly
✅ Helpful for debugging or analyzing balance/skew quickly


📌 Examples

1️⃣ **Balanced Tree (3 levels)**
        1
       / \
      2   3
     / \ / \
    4  5 6  7
Custom:   ['1', '2', '3', 'N4N', 'N5N', 'N6N', 'N7N']
BFS:      [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None]
DFS:      [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]


2️⃣ **Left Skewed Tree (5 levels)**
            1
           /
          2
         /
        3
       /
      4
     /
    5
Custom:   ['1N', '2N', '3N', '4N', 'N5N']
BFS:      [1, 2, None, 3, None, 4, None, 5, None, None]
DFS:      [1, 2, 3, 4, 5, None, None, None, None, None, None]

3️⃣ **Right Skewed Tree (5 levels)**
    1
     \
      2
       \
        3
         \
          4
           \
            5
Custom:   ['N1', 'N2', 'N3', 'N4', 'N5N']
BFS:      [1, None, 2, None, 3, None, 4, None, 5, None]
DFS:      [1, None, 2, None, 3, None, 4, None, 5, None, None]

📌 Outcome
→ Passed all GeeksforGeeks test cases successfully
→ Balanced tree, left-skewed, and right-skewed examples serialize neatly
→ Gave me a fresh way of *thinking about encoding structure*
→ It's a reminder that sometimes, exploring beyond the “standard” solution uncovers new perspectives

🧠 This approach is not standard — but it definitely helped me sharpen my DSA thinking and problem re-imagination skills.

💬 Open to Feedback
Would love to hear if you see hidden drawbacks, better optimizations, or creative extensions of this idea.

🧼 For a clean, well-documented version (including BFS & DFS solutions):
👉 [GitHub / GFG link once you upload]

🤝 Let's connect if you enjoy discussing unconventional problem-solving techniques!

#Python #DSA #CodingChallenge #BinaryTree #Serialization #GeeksForGeeks #DevJourney #CodingJourney #CodeNewbie #OutOfTheBoxThinking #ProblemSolving #100DaysOfCode #LearningByDoing #GFG160
"""
