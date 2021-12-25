#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        total = 0
        for i in s:
            total += values[i]
        return total
        
# @lc code=end