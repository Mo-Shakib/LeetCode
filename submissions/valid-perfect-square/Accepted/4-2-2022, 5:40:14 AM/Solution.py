// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = int(num ** 0.5)
        if x ** 2 == num:
            return True
        return False