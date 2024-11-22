# Valid Parentheses
**URL**: [https://leetcode.com/problems/valid-parentheses/description/](https://leetcode.com/problems/valid-parentheses/description/)

**Description:**

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

 __Example 1:__
```
Input: s = "()"
Output: true
```

 __Example 2:__
```
Input: s = "()[]{}"
Output: true
```

 __Example 3:__
```
Input: s = "(]"
Output: false
```

 __Example 4:__
```
Input: s = "([])"
Output: true
```

 __Constraints:__
```
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
```

**Solution Code**:
```python
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

```
