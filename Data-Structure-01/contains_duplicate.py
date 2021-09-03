# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        if len(nums) == len(x):
            return False
        return True