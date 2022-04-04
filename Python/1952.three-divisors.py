#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#
# https://leetcode.com/problems/three-divisors/description/
#
# algorithms
# Easy (56.51%)
# Likes:    215
# Dislikes: 15
# Total Accepted:    25.2K
# Total Submissions: 44.5K
# Testcase Example:  '2'
#
# Given an integer n, return true if n has exactly three positive divisors.
# Otherwise, return false.
# 
# An integer m is a divisor of n if there exists an integer k such that n = k *
# m.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.
# 
# 
# Example 2:
# 
# 
# Input: n = 4
# Output: true
# Explantion: 4 has three divisors: 1, 2, and 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count == 3:
            return True
        else:
            return False
        
# @lc code=end

