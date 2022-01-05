#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        dic = {}
        # counting total number of appearance of an element
        for ele in nums2:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1
        
        for i in nums1:
            # if there are enough number of element then append it to result [], and decrease number of appearance by 1
            if i in nums2 and dic[i] > 0:
                output.append(i)
                dic[i] -= 1
        return output
        
        
# @lc code=end

