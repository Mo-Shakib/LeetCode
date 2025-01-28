// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        for i in range(0, n+1):
            a ^= i
        b = 0
        for i in nums:
            b ^= i
        
        return a ^ b

        