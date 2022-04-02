#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (34.52%)
# Likes:    1301
# Dislikes: 458
# Total Accepted:    129.6K
# Total Submissions: 375.5K
# Testcase Example:  '5'
#
# Given a non-negative integer c, decide whether there're two integers a and b
# such that a^2 + b^2 = c.
# 
# 
# Example 1:
# 
# 
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# Example 2:
# 
# 
# Input: c = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= c <= 2^31 - 1
# 
# 
#

# @lc code=start
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        
        if c <= 2:
            return True
        
        while (a<=b):
            result = (a*a) + (b*b)
            if result == c: return True
            if result < c:  a += 1
            else: b -= 1
        return False
# @lc code=end

