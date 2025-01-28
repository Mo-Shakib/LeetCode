// https://leetcode.com/problems/arranging-coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        staircase = 0
        while (staircase <= n):
            n -= staircase
            staircase += 1
        return staircase - 1