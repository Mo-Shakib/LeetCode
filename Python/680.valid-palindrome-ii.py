#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (38.52%)
# Likes:    4261
# Dislikes: 254
# Total Accepted:    425.1K
# Total Submissions: 1.1M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_r = s[::-1]
        n = 0
        if s == s_r:
            return True
        if len(s) == 1:
            return True

        for i,j in zip(s,s_r):
            if i != j:
                n += 1
            if n > 3:
                break
        if len(s) < 4 and n > 1:
            return False

        elif n > 2:
            return False
        
        return True        
# @lc code=end

