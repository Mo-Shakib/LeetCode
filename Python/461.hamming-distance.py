#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (74.32%)
# Likes:    2889
# Dislikes: 196
# Total Accepted:    455.9K
# Total Submissions: 613.3K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, return the Hamming distance between them.
# 
# 
# Example 1:
# 
# 
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
# Example 2:
# 
# 
# Input: x = 3, y = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 0 <= x, y <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = bin(x ^ y)[2:]
        return str(res).count('1')
        
# @lc code=end
