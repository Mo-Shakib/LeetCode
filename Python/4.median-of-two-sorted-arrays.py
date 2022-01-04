#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for element in nums2:
            nums1.append(element)
        
        nums1.sort()
        lenth = len(nums1)
        
        if lenth % 2 == 0:
            n1 = lenth // 2
            n2 = n1 - 1
            return (nums1[n1] + nums1[n2])/2
        else:
            return nums1[lenth//2]
            
        
# @lc code=end

