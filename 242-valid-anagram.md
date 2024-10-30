# Valid Anagram
**URL**: [https://leetcode.com/problems/valid-anagram/description/](https://leetcode.com/problems/valid-anagram/description/)

**Description:**

Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

 __Example 1:__
```
Input: s = "anagram", t = "nagaram"
Output: true
```

 __Example 2:__
```
Input: s = "rat", t = "car"
Output: false
```

 __Constraints:__
```
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
```
Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?

**Solution Code**:
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for i, j in zip(s,t):
            if i == j:
                continue
            elif i != j:
                return False
        return True


```
