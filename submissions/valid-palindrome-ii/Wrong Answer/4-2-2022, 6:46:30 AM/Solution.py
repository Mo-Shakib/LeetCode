// https://leetcode.com/problems/valid-palindrome-ii

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