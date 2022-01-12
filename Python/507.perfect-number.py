#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (37.44%)
# Likes:    499
# Dislikes: 801
# Total Accepted:    95.3K
# Total Submissions: 254.4K
# Testcase Example:  '28'
#
# A perfect number is a positive integer that is equal to the sum of its
# positive divisors, excluding the number itself. A divisor of an integer x is
# an integer that can divide x evenly.
# 
# Given an integer n, return true if n is a perfect number, otherwise return
# false.
# 
# 
# Example 1:
# 
# 
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# 
# 
# Example 2:
# 
# 
# Input: num = 7
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 10^8
# 
# 
#

# @lc code=start
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [1]
        if num == 1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                divisors.extend([i,num/i])
                
        if sum(set(divisors)) == num:
            return True
        return False
        
# @lc code=end

