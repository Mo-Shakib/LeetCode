// https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        res = nums1 & nums2
        
        return list(res)