#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#
# https://leetcode.com/problems/xor-operation-in-an-array/description/
#
# algorithms
# Easy (84.09%)
# Likes:    696
# Dislikes: 272
# Total Accepted:    111K
# Total Submissions: 132K
# Testcase Example:  '5\n0'
#
# You are given an integer n and an integer start.
# 
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n ==
# nums.length.
# 
# Return the bitwise XOR of all elements of nums.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8)
# = 8.
# Where "^" corresponds to bitwise XOR operator.
# 
# 
# Example 2:
# 
# 
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) =
# 8.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length
# 
# 
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        res = nums[0]
        for i in range(1, n):
            res ^= nums[i]
        return res
        
# @lc code=end

