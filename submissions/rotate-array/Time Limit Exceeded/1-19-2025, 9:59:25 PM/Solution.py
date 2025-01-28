// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            prev = nums[0]
            for i in range(len(nums)):
                temp =  nums[i]
                nums[i] = prev
                prev = temp

            nums[0] = prev
            k -= 1

        