# Merge Strings Alternately
**URL**: [https://leetcode.com/problems/merge-strings-alternately/description/](https://leetcode.com/problems/merge-strings-alternately/description/)

**Description**

**Solution Code**:
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = min(len(word1), len(word2))
        res = ''
        for i in range(m):
            res += word1[i] + word2[i]

        if m == len(word1):
            return res + word2[m:]
        else:
            return res + word1[m:]

```
