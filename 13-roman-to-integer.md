# Roman to Integer
**URL**: [https://leetcode.com/problems/roman-to-integer/description/](https://leetcode.com/problems/roman-to-integer/description/)

**Description**

 __Example 1:__
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

 __Example 2:__
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

 __Example 3:__
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

 __Constraints:__
```
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
```

**Solution Code**:
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I' : 1,
            'V': 5,
            'X': 10,
            'L':50,
            'C': 100,
            'D':500,
            'M':1000
        }
        digit = []
        res = 0
        for char in s:
            digit.append(vals[char])

        digit.append(0)
        for i in range(len(digit)-1):
            if digit[i] >= digit[i+1]:
                res += digit[i]
            else:
                res -= digit[i]

        return res

```
