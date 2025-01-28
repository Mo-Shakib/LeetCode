// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')
        nums = set(nums)
        for i in nums:
            if abs(i) < abs(res):
                res = i
            elif i == abs(res):
                if i > res:
                    res = i
        return res