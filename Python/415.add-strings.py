#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (51.34%)
# Likes:    2772
# Dislikes: 495
# Total Accepted:    421.8K
# Total Submissions: 820.4K
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
# 
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
# 
# 
# Example 1:
# 
# 
# Input: num1 = "11", num2 = "123"
# Output: "134"
# 
# 
# Example 2:
# 
# 
# Input: num1 = "456", num2 = "77"
# Output: "533"
# 
# 
# Example 3:
# 
# 
# Input: num1 = "0", num2 = "0"
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:    
        ans = int(num1) + int(num2)
        return str(ans)
        
# @lc code=end

