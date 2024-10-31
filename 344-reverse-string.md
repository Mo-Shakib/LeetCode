# Reverse String
**URL**: [https://leetcode.com/problems/reverse-string/description/](https://leetcode.com/problems/reverse-string/description/)

**Description:**

Write a function that reverses a string. The input string is given as an
array of characters s.
You must do this by modifying the input array in-place with O(1) extra
memory.

 __Example 1:__
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

 __Example 2:__
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

 __Constraints:__
```
1 <= s.length <= 10^5
s[i] is a printable ascii character.
```

**Solution Code**:
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        s = s[:-1]
        return s
        """
        s[:] = s[::-1]
        return s

```
