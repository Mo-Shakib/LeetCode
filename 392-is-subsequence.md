# Is Subsequence
**URL**: [https://leetcode.com/problems/is-subsequence/description/](https://leetcode.com/problems/is-subsequence/description/)

**Description**
A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).

 __Example 1:__
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

 __Example 2:__
```
Input: s = "axc", t = "ahbgdc"
Output: false
```

 __Constraints:__
```
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
```
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
>= 10^9, and you want to check one by one to see if t has its subsequence. In
this scenario, how would you change your code?

**Solution Code**:
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        found = 0
        x = 0
        for i in s:
            while x < len(t) and t[x] != i:
                x += 1
            if x < len(t):
                x += 1
                found += 1
            else:
                break

        return found == len(s)

```
