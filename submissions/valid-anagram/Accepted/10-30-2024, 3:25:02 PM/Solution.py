// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        s = sorted(s)
        t = sorted(t)
        
        for i, j in zip(s,t):
            if i == j:
                continue
            elif i != j:
                return False
        return True


        