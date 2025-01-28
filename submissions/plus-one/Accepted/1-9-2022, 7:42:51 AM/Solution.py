// https://leetcode.com/problems/plus-one

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
        