// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for x in range(len(nums)):
            count = nums.count(nums[x])
            if count == 1:
                return nums[x]
            if nums[x] not in dic:
                dic[count] = nums[x]
                
        return dic[1]
    
        
        