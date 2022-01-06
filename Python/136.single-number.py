#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for x in range(len(nums)):
            count = nums.count(nums[x])
            if count == 1:
                # best case
                return nums[x]
            if nums[x] not in dic:
                dic[count] = nums[x]
        # wrost case
        return dic[1]

# Time complexity: O(n)
        
# @lc code=end

