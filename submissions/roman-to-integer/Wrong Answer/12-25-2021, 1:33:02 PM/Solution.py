// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        total = 0
        for i in s:
            total += values[i]
        return total
        