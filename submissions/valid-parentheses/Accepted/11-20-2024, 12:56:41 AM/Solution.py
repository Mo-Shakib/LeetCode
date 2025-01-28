// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        open = ['(','{','[']
        stack = []
        for braket in s:
            if braket in open:
                stack.append(braket)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if (braket == ')' and popped != '(') or (braket == '}' and popped != '{') or (braket == ']' and popped != '['):
                    return False
        return (len(stack) == 0)
              