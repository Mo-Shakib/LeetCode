# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

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