// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        nums = set(nums)
        
        for i in nums:
            if (abs(i)-0) < abs(res):
                res = i
            else:
                continue
        return res