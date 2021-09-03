# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a dictionary to store the number and index
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
                
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))