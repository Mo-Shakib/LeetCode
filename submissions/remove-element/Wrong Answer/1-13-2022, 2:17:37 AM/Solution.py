// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for item in nums:
            if item == val:
                nums.remove(item)
        return len(nums)
    