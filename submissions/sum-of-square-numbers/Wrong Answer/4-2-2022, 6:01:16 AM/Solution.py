// https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 1
        b = int((c-1)**0.5)
        res = (a+b)**2 - 2*a*b
        if c == res:
            return True
        return False