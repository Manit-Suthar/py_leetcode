class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0  # Tracks unmatched ')' that need a '(' at the front
        close_needed = 0 # Tracks unmatched '(' that need a ')' at the back
        
        for ch in s:
            if ch == "(":
                # We found an opening bracket; it will need a closing partner
                close_needed += 1
            elif ch == ")":
                if close_needed > 0:
                    # A matching '(' is available, cancel it out
                    close_needed -= 1
                else:
                    # No '(' is available; this ')' is permanently unmatched
                    open_needed += 1
                    
        # Total additions is the sum of both unmatched sets
        return open_needed + close_needed

#stack based approach O(n)
# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         stack = []
#         unmatched_close = 0 # Tracks ')' that couldn't find a '('
        
#         for ch in s:
#             if ch == "(":
#                 # Push open brackets onto the stack to match later
#                 stack.append(ch)
#             elif ch == ")":
#                 if stack:
#                     # A '(' is available on top of the stack; pop it off
#                     stack.pop()
#                 else:
#                     # The stack is empty; this ')' is stranded
#                     unmatched_close += 1
                    
#         # Total additions is the stranded ')' plus whatever '(' remain on the stack
#         return unmatched_close + len(stack)

    
print(Solution().minAddToMakeValid("()))(("))