// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        open = ['(','{','[']
        close = [')','}',']']

        dump = []
        stack = []
        for i in s:
            if i in open:
                stack.append(i)
            
            elif i in close and len(stack) != 0:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                elif len(stack) == 0 and i in close:
                    return False
        
        if len(stack) == 0:
            return True
        return False
        