#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.86%)
# Likes:    2068
# Dislikes: 226
# Total Accepted:    344.7K
# Total Submissions: 803.7K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = int(num ** 0.5)
        if x ** 2 == num:
            return True
        return False

        
# @lc code=end

