#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)
        
# @lc code=end

