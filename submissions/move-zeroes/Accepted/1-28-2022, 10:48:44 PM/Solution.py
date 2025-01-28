// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                x += 1