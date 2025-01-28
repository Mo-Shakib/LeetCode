// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        nums = set(nums)
        
        neg = []
        pos = []

        for i in nums:
            if (abs(i)-0) < abs(res):
                if i >= 0:
                    pos.append(i)
                else:
                    neg.append(i)
                res = i
            else:
                continue
        
        if len(pos) >= len(neg):
            return abs(res)
        return res