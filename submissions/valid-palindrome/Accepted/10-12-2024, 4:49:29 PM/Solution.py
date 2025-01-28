// https://leetcode.com/problems/valid-palindrome

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        if s.lower() == s[::-1].lower():
            return True
        else:
            return False
