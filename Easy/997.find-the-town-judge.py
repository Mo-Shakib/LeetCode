#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = {} # to store key value pairs
        # there is only one person and he does not trust himself
        if len(trust) == 0 and n == 1:
            return 1
        # there are more than one perosn and nobody trust anyone!
        if n > 1 and len(trust) == 0:
            return -1
        
        # looping through the list and getting the trust values of every person. If a person is trusted by someone then his trust value increases else decreases.
        
        for (a, b) in trust:
            
            if a not in trusted:
                trusted[a] = -1
            else:
                trusted[a] -= 1
            
            if b not in trusted:
                trusted[b] = 1
            else:
                trusted[b] += 1
        
        # if a person is trusted by n-1 people then he will be the judge, else there is no judge!
        for key, value in trusted.items():
            if value == n -1:
                return key
        return -1
        
# @lc code=end

