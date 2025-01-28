// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                if nums.count(nums[i]) == 1:
                    return nums[i]
                elif nums.count(nums[i+1]) == 1:
                    return nums[i+1]
        
        