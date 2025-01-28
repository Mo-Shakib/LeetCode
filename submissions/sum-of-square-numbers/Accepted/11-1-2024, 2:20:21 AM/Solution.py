// https://leetcode.com/problems/sum-of-square-numbers

from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        
        if c <= 2:
            return True
        
        while (a<=b):
            result = (a*a) + (b*b)
            if result == c:
                return True
            if result < c:
                a += 1
            else:
                b -= 1
        return False
        