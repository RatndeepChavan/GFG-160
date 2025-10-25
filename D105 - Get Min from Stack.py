"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/get-minimum-element-from-stack

Implement a class SpecialStack that supports following operations:

push(x) - Insert an integer x into the stack.
pop() - Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMin() - Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
isEmpty() -  Return true if stack is empty, else false
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call push(x)
2:  Call pop()
3: Call peek()
4: Call getMin()
5: Call isEmpty()
The driver code will process the queries, call the corresponding functions, and print the outputs of peek(), getMin(), isEmpty() operations.
You only need to implement the above five functions.

Examples:
Input: q = 7, queries[][] = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
Output: [3, 2, 1]
Explanation: 
push(2): Stack is [2]
push(3): Stack is [2, 3]
peek(): Top element is 3
pop(): Removes 3, stack is [2]
getMin(): Minimum element is 2
push(1): Stack is [2, 1]
getMin(): Minimum element is 1

Input: q = 4, queries[][] = [[1, 4], [1, 2], [4], [3], [5]]
Output: [2, 2, false]
Explanation: 
push(4): Stack is [4]
push(2): Stack is [4, 2]
getMin(): Minimum element is 2
peek(): Top element is 2
isEmpty(): false

Constraints:
1 ≤ q ≤ 105
0 ≤ values on the stack ≤ 109
"""

# ------------------------------------------------------------------
# * 🟢 SpecialStack — Stack supporting getMin() in O(1)
# ------------------------------------------------------------------
class SpecialStack:
    """
    🧩 Problem:
    ------------
    Design a stack that supports:
        - push(x)
        - pop()
        - peek()
        - getMin()   → all in O(1) time

    Without using an extra stack for minima.

    💡 Core Idea:
    --------------
    Use one stack and one variable (`min_val`) to track the current minimum.
    Whenever a new element ≤ current min is pushed, we first push the *previous min*
    into the stack as a **backup**, then push the new value and update `min_val`.

    So the stack stores both:
        1️⃣ Actual pushed values
        2️⃣ Backups of previous minima (just before each new minimum)

    On popping a min element, we restore the previous min by popping the backup.

    ✅ Time Complexity:
        - push(), pop(), getMin() → O(1)
    ✅ Space Complexity:
        - O(1) extra (only `min_val`, no secondary stack)
    """

    def __init__(self):
        self.stack = []
        self.min_val = float("inf")  # start with sentinel +∞

    # --------------------------------------------------------------
    # * push(x): Insert element while maintaining min tracking
    # --------------------------------------------------------------
    def push(self, x):
        """
        Pushes an element onto the stack while maintaining the minimum.

        💡 Trick:
        If `x <= min_val`, we:
            - Push the *previous* min onto stack as backup
            - Update `min_val` to new value
        Then push `x` itself.

        ❓Why?
        When we later pop this min, we’ll restore old min from backup.
        """
        if self.stack:
            if x <= self.min_val:
                self.stack.append(self.min_val)  # 💾 store old min
                self.min_val = x                 # 🔄 update min
        else:
            # first element — just set min
            self.min_val = x

        self.stack.append(x)

    # --------------------------------------------------------------
    # * pop(): Remove top element, restore min if needed
    # --------------------------------------------------------------
    def pop(self):
        """
        Pops top element. If it was the current min, restore previous min
        from the backup value stored just beneath it.
        """
        if self.stack:
            val = self.stack.pop()

            # ❓If popped element *was* the min:
            # then previous min sits right below → pop and restore
            if val == self.min_val:
                if self.stack:
                    self.min_val = self.stack.pop()  # ♻️ restore old min
                else:
                    self.min_val = float("inf")      # stack empty → reset

    # --------------------------------------------------------------
    # * peek(): Return top element
    # --------------------------------------------------------------
    def peek(self):
        """Return top of stack (or -1 if empty)."""
        return self.stack[-1] if self.stack else -1

    # --------------------------------------------------------------
    # * getMin(): Return current minimum
    # --------------------------------------------------------------
    def getMin(self):
        """Return the current minimum element (or -1 if empty)."""
        return self.min_val if self.stack else -1

    # --------------------------------------------------------------
    # * isEmpty(): Return True if stack is empty
    # --------------------------------------------------------------
    def isEmpty(self):
        """Check if stack is empty."""
        return len(self.stack) == 0


# ------------------------------------------------------------------
# * 🔸 2. Alternative Approach — Using Two Stacks
# ------------------------------------------------------------------

class SpecialStackAlt:
    """
    💡 Alternative (Simpler but uses O(N) extra space):
    Maintain two stacks:
      - main_stack: normal stack values
      - min_stack: track min at each level
    """

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        self.main_stack.append(x)
        # Push new min or repeat previous min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.main_stack:
            self.min_stack.pop()
            return self.main_stack.pop()

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1

    def peek(self):
        return self.main_stack[-1] if self.main_stack else -1

    def isEmpty(self):
        return not bool(self.main_stack)

