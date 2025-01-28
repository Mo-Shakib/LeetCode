// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs

class Solution:
    def checkString(self, s: str) -> bool:
        check = []
        for i in s:
            if i == 'a' and check.count('b') == 1:
                check.append('a')
            if i == 'b' and check.count('b') == 0:
                check.append('b')
        if len(check) == 2:
            return False
        return True
        