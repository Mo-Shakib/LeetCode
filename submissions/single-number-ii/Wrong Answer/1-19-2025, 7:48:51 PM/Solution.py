// https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in range(32):
            count = 0
            for i in range(len(nums)):
                if (nums[i] & (1 << x) != 0):
                    count += 1

            if count % 3 != 0:
                ans = ans | (1 << x)
        
        return ans
        
        