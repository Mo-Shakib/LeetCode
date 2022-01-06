#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                if nums.count(nums[i]) == 1:
                    return nums[i]
                elif nums.count(nums[i+1]) == 1:
                    return nums[i+1]
        
        
# @lc code=end

