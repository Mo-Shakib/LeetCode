# Sum of Square Numbers
**URL**: [https://leetcode.com/problems/sum-of-square-numbers/description/](https://leetcode.com/problems/sum-of-square-numbers/description/)

**Description:**

Given a non-negative integer c, decide whether there're two integers a and b
such that a^2 + b^2 = c.

 __Example 1:__
```
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
```

 __Example 2:__
```
Input: c = 3
Output: false
```

 __Constraints:__
```
0 <= c <= 2^31 - 1
```

**Solution Code**:
```python
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))

        if c <= 2:
            return True

        while (a<=b):
            result = (a*a) + (b*b)
            if result == c:
                return True
            if result < c:
                a += 1
            else:
                b -= 1
        return False

```
