// https://leetcode.com/problems/is-subsequence

import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        found = 0
        for i in s:
            x = 0
            for j in t[x:]:
                if i == j:
                    found += 1
                    x += 1
                else:
                    continue
                    # x += 1
        
        return found == len(s)
            

        