class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {
             "}": "{",
             ")" : "(",
             "]" : "["}

        for c in s:
            if c in "{([":
                stack.append(c)
            else:
                if not stack or stack[-1] != parenthesis[c]:
                    return False
                else:
                    stack = stack[:-1]
        
        return True if not stack else False