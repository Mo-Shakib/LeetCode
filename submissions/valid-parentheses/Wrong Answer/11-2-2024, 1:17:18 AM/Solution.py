// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        open = ['(','{','[']

        stack = []
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        