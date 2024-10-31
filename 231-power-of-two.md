# Power of Two
**URL**: [https://leetcode.com/problems/power-of-two/description/](https://leetcode.com/problems/power-of-two/description/)

**Description:**

Given an integer n, return true if it is a power of two. Otherwise, return
false.
An integer n is a power of two, if there exists an integer x such that n ==
2^x.

 __Example 1:__
```
Input: n = 1
Output: true
Explanation: 2^0 = 1
```

 __Example 2:__
```
Input: n = 16
Output: true
Explanation: 2^4 = 16
```

 __Example 3:__
```
Input: n = 3
Output: false
```

 __Constraints:__
```
-2^31 <= n <= 2^31 - 1
```
Follow up: Could you solve it without loops/recursion?

**Solution Code**:
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n==1):
            return True

        n_bin = bin(n)
        n_bin = n_bin[2:]

        if (n_bin[0]!= '1'):
            return False

        elif (n_bin.count('1')>1):
            return False

        return True

```
