// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
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
        return True
        