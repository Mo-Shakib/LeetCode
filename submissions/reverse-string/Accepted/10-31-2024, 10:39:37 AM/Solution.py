// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        s = s[:-1]
        return s
        """
        s[:] = s[::-1]
        return s
        