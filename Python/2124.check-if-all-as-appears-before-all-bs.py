#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
#
# algorithms
# Easy (73.45%)
# Likes:    109
# Dislikes: 1
# Total Accepted:    14.7K
# Total Submissions: 20.1K
# Testcase Example:  '"aaabbb"'
#
# Given a string s consisting of only the characters 'a' and 'b', return true
# if every 'a' appears before every 'b' in the string. Otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and
# 5.
# Hence, every 'a' appears before every 'b' and we return true.
# 
# 
# Example 2:
# 
# 
# Input: s = "abab"
# Output: false
# Explanation:
# There is an 'a' at index 2 and a 'b' at index 1.
# Hence, not every 'a' appears before every 'b' and we return false.
# 
# 
# Example 3:
# 
# 
# Input: s = "bbb"
# Output: true
# Explanation:
# There are no 'a's, hence, every 'a' appears before every 'b' and we return
# true.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s[i] is either 'a' or 'b'.
# 
# 
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == 'b':
                for j in range(i, len(s)):
                    if s[j] == 'a':
                        return False
                return True
            else:
                x = True
        return x
        
# @lc code=end

