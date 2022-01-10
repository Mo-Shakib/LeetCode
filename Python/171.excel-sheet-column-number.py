#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for x in range(len(columnTitle)):
            res += 26**(len(columnTitle)-x-1) * (ord(columnTitle[x]) - ord('A') + 1)
        return res
        
# @lc code=end

