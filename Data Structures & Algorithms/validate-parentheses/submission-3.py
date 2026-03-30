class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack:
                    if ((c == ')' and stack[-1] != '(') or (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '[')):
                        return False
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0