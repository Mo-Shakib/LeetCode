#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.07%)
# Likes:    18142
# Dislikes: 4621
# Total Accepted:    3.9M
# Total Submissions: 8.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the smallest length element
        smallest_length_element = min(strs, key=len)
        # Get the length of the smallest element
        smallest_length = len(smallest_length_element)
        res = ''
        for i in range(smallest_length):
            x = len(strs)
            y = 0
            for element in strs:
                if element[i] == smallest_length_element[i]:
                    y += 1
                    if y == x:
                        res += element[i]
                        y = 0
                else:
                    return res
        return res
        
# @lc code=end

