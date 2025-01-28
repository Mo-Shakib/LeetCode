// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = [x for x in nums1 if x in nums2]
        # output = []
        # for i in nums1:
        #     if i in nums2:
        #         output.append(i)
        # return output
        return nums3
        
        