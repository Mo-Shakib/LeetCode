// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')
        neg = []
        pos = []

        for i in nums:
            if (abs(i)) < abs(res):
                res = i
            elif abs(i) == abs(res):
                res = i
        return res