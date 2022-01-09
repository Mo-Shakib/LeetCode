#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        value = ''
        res = []
        
        for i in digits:
            value += str(i)
        
        value = int(value)
        value += 1
        
        for i in str(value):
            res.append(int(i))
            
        return res
        
# @lc code=end
