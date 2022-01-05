#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = {}
        if len(trust) == 0 and n == 1:
            return 1
        if n > 1 and len(trust) == 0:
            return -1
        
        for (a, b) in trust:
            if a not in trusted:
                trusted[a] = -1
            else:
                trusted[a] -= 1
            
            if b not in trusted:
                trusted[b] = 1
            else:
                trusted[b] += 1
        
        for key, value in trusted.items():
            if value == n -1:
                return key
        return -1
        
# @lc code=end

