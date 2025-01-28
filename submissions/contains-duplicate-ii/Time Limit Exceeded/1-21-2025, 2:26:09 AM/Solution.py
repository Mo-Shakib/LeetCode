// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        i = 0
        j = k+1
        x = 0

        while x < len(nums):
            c = nums[i:j].count(nums[i])
            if c > 1:
                return True
            i += 1
            j += 1
            x += 1
            
        return False




        
        

            

