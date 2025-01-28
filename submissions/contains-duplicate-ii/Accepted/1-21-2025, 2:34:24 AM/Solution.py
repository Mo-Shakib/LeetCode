// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = []

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.append(nums[i])

            if len(window) > k:
                window.pop(0)

        return False



        
        

            

