// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        found = 0
        x = 0
        for i in s:
            for j in t[x:]:
                if i == j:
                    found += 1
                    x += 1
                else:
                    continue
                    x += 1
        
        return found == len(s)
            

        