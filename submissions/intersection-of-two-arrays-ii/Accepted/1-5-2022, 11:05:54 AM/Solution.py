// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        dic = {}
        for ele in nums2:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1
        
        for i in nums1:
            if i in nums2 and dic[i] > 0:
                output.append(i)
                dic[i] -= 1
        return output
        
        