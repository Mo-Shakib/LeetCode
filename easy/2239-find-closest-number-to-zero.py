#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#
# https://leetcode.com/problems/find-closest-number-to-zero/description/
#
# algorithms
# Easy (46.50%)
# Likes:    629
# Dislikes: 46
# Total Accepted:    118.9K
# Total Submissions: 255.8K
# Testcase Example:  '[-4,-2,1,4,8]'
#
# Given an integer array nums of size n, return the number with the value
# closest to 0 in nums. If there are multiple answers, return the number with
# the largest value.
# 
# Example 1:
# 
# 
# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is
# returned.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')
        nums = set(nums)
        for i in nums:
            if abs(i) < abs(res):
                res = i
            elif i == abs(res):
                if i > res:
                    res = i
        return res
        
# @lc code=end

