// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for item in nums:
            if item != val:
                nums[idx] = item
                idx += 1
        return idx
    