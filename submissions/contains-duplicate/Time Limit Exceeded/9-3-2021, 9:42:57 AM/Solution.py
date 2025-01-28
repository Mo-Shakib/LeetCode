// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = []
        for i in nums:
            if i not in x:
                x.append(i)
        if len(nums) == len(x):
            return False
        return True