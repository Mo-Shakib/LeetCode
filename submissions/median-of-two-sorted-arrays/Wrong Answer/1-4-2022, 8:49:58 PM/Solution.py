// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for element in nums2:
            nums1.append(element)
        nums1.sort()
        lenth = len(nums1)
        if lenth % 2 == 0:
            n1 = lenth // 2
            n2 = n1 - 1
            median = (nums1[n1] + nums2[n2])/2
            return median
        else:
            return nums1[lenth//2]
            
        