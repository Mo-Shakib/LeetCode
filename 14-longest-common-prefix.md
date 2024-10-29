# Longest Common Prefix
**URL**: [https://leetcode.com/problems/longest-common-prefix/description/](https://leetcode.com/problems/longest-common-prefix/description/)

**Description**
Write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string "".

 __Example 1:__
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

 __Example 2:__
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

 __Constraints:__
```
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
@lc code=start
Find the smallest length element
```

**Solution Code**:
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the smallest length element
        smallest_length_element = min(strs, key=len)
        # Get the length of the smallest element
        smallest_length = len(smallest_length_element)
        res = ''
        for i in range(smallest_length):
            x = len(strs)
            y = 0
            for element in strs:
                if element[i] == smallest_length_element[i]:
                    y += 1
                    if y == x:
                        res += element[i]
                        y = 0
                else:
                    return res
        return res

```
