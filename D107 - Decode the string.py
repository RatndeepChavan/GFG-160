"""
Link : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/stack-gfg-160/problem/decode-the-string2444

Given an encoded string s, decode it by expanding the pattern k[substring], where the substring inside brackets is written k times. k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets. Return the final decoded string.

Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
Inner substring “2[ca]” breakdown into “caca”.
Now, new string becomes “3[bcaca]”
Similarly “3[bcaca]” becomes “bcacabcacabcaca” which is final result.

Input: s = "3[ab]"
Output: "ababab"
Explanation: The substring "ab" is repeated 3 times giving "ababab".

Constraints:
1 ≤ |s| ≤ 105 
1 ≤ k ≤ 100
"""

# ------------------------------------------------------------------
# ! 🔴 1. Reverse Traversal + Single Stack (Your Unique Approach)
# ------------------------------------------------------------------

class Solution:
    """
    💡 Problem:
    ------------
    Given an encoded string `s`, decode it.
    The encoding rule is: k[encoded_string], where the encoded_string 
    inside the square brackets is repeated exactly k times.

    Example:
        Input  ➜ "3[a2[bc]]"
        Output ➜ "abcbcabcbcabcbc"

    🧠 Unique Reverse Approach:
    ----------------------------
    Instead of parsing from left → right (as usually done),
    we start from **right → left** and use **a single stack**.

    Why it's cool:
    ✅ Avoids recursion entirely  
    ✅ Uses only one stack (not separate for count & substring)  
    ✅ Naturally builds substrings in reverse and expands cleanly

    🪄 Core Logic:
    ---------------
    - Traverse `s` from end to start.
    - When encountering a number → repeat current substring.
    - When encountering '[' or ']' → control grouping and stack order.
    - Build partial results and push to stack as needed.

    📊 Complexity:
    --------------
    ⏱️ **Time:** O(N * K)  (K = average repeat count)
    🧠 **Space:** O(N)     (stack and substring building)
    """

    def decodedString(self, s):
        stack = []           # stores partial decoded strings and control chars
        ptr = len(s) - 1     # pointer starts from end
        st = ""              # current substring under processing

        while ptr >= 0:
            ch = s[ptr]

            # ----------------------------------------------------------
            # * 🔢 Case 1: When digit found → form number (can be multi-digit)
            # ----------------------------------------------------------
            if ch.isdigit():
                tmp = None
                while ch.isdigit():
                    # ? Build number in reverse (since we’re scanning backward)
                    tmp = ch + tmp if tmp else ch
                    ptr -= 1
                    ch = s[ptr]

                # ? Repeat substring 'st' tmp times
                st *= int(tmp)

                # Push the expanded part to stack (if non-empty)
                if st:
                    stack.append(st)
                    st = ""
                continue  # already adjusted ptr

            # ----------------------------------------------------------
            # * 🧱 Case 2: Opening bracket '[' — collect substring till ']'
            # ----------------------------------------------------------
            elif ch == "[":
                while stack[-1] != "]":
                    st += stack.pop()
                stack.pop()  # remove matching ']'

            # ----------------------------------------------------------
            # * 🚪 Case 3: Closing bracket ']' — push marker & current substring
            # ----------------------------------------------------------
            elif ch == "]":
                if st:
                    stack.append(st)
                    st = ""
                stack.append(ch)

            # ----------------------------------------------------------
            # * 🔤 Case 4: Alphabetic character — prepend to substring
            # ----------------------------------------------------------
            else:
                st = ch + st

            ptr -= 1  # move left

        # ----------------------------------------------------------
        # * 🧩 Final: Rebuild decoded string (ignore any brackets)
        # ----------------------------------------------------------
        res = ""
        for ch in stack:
            if ch not in ["[", "]"]:
                res = ch + res

        return res


# ------------------------------------------------------------------
# ! 🟢 2. Forward Traversal + Two Stacks (Standard Solution)
# ------------------------------------------------------------------

class SolutionForward:
    """
    🧩 Approach:
    ------------
    - Traverse **left → right**.
    - Use:
        🔹 `num_stack` → stores repeat counts
        🔹 `str_stack` → stores partial results
    - On seeing '[', push current number and new empty substring.
    - On seeing ']', pop from both stacks and expand.

    📘 Example:
    ------------
        s = "3[a2[c]]"

        Step 1: push 3, start new substring
        Step 2: inside bracket: push 2, start new substring
        Step 3: on ']', expand "c" * 2 → "cc"
        Step 4: next ']', expand "a" + "cc" * 3 → "accaccacc"

    📊 Complexity:
    --------------
    ⏱️ Time  → O(N * K)
    🧠 Space → O(N)
    """

    def decodedString(self, s):
        num_stack = []  # holds repeat counts
        str_stack = [""]  # holds partial substrings
        num = 0

        for ch in s:
            # 🔢 Form full number if consecutive digits
            if ch.isdigit():
                num = num * 10 + int(ch)

            # 🧱 Opening bracket → start a new level
            elif ch == "[":
                num_stack.append(num)
                str_stack.append("")  # start new substring
                num = 0

            # 🚪 Closing bracket → pop & expand
            elif ch == "]":
                sub = str_stack.pop()
                repeat = num_stack.pop()
                str_stack[-1] += sub * repeat  # merge back

            # 🔤 Normal char → add to top of string stack
            else:
                str_stack[-1] += ch

        # Top of stack is final decoded string
        return str_stack[-1]


# ------------------------------------------------------------------
# ! 🟡 3. Recursive DFS (Elegant & Intuitive)
# ------------------------------------------------------------------

class SolutionRecursive:
    """
    🧩 Approach:
    ------------
    - Use recursion to handle nested brackets naturally.
    - Each recursive call decodes substring until its matching ']'.
    - On seeing digit: form number.
    - On seeing '[', recursively decode that inner section.
    - On seeing ']', return accumulated string and index.

    📘 Example:
    ------------
        s = "3[a2[bc]]"
        decode(0):
        → finds 3
        → calls decode(2): decodes "a2[bc]" → "abcbc"
        → returns "abcbcabcbcabcbc"

    📊 Complexity:
    --------------
    ⏱️ Time  → O(N * K)
    🧠 Space → O(N) recursion depth (for nested structures)
    """

    def decodedString(self, s):
        def dfs(i):
            res, num = "", 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == "[":
                    sub, i = dfs(i + 1)
                    res += sub * num
                    num = 0
                elif s[i] == "]":
                    return res, i
                else:
                    res += s[i]
                i += 1
            return res, i

        decoded, _ = dfs(0)
        return decoded

"""
📊  Comparison Summary
#	Approach	               Direction	    Uses	    Recursion   Time	 Space	 Comments
1	Reverse + Single Stack     Right → Left	    1 Stack	    ❌          O(N·K)	O(N)	Smart, minimal, elegant
2	Forward + Two Stacks	   Left → Right	    2 Stacks	❌	       O(N·K)	O(N)	Standard textbook approach
3	Recursive DFS	           Left → Right	    None	    ✅	       O(N·K)	O(N)	Clean but may hit recursion depth
"""