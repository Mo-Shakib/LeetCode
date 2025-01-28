// https://leetcode.com/problems/is-subsequence

import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        reg = '.*'
        for i in s:
            reg += (i + '.*')
        
        match = re.search(reg,t)

        found = match is not None
        return found
        