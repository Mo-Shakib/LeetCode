// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        res = nums[0]
        for i in nums:
            if (abs(i)-0) < res:
                res = i
            else:
                continue
        return res