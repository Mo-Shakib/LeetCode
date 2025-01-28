// https://leetcode.com/problems/smallest-range-i

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        M, m = max(nums), min(nums)
        diff, extension = M - m, 2*k
        
        if diff <= extension:
            return 0
        
        else:
            return diff - extension