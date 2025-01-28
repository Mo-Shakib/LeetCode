// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1001
        for i in nums:
            if (abs(i)-0) < res:
                res = abs(i)
            else:
                continue
        return res