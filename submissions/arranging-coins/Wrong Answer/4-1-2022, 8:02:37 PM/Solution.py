// https://leetcode.com/problems/arranging-coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        completed = 0
        x = 0
        for i in range(1,n+1):
            if i <= n:
                x += 1
                n -= i
            else:
                return x
