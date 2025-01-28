// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        found = 0
        x = 0
        for i in s:
            while x < len(t) and t[x] != i:
                x += 1  
            if x < len(t): 
                x += 1 
                found += 1
            else:
                break  

        return found == len(s)
            

        