// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
                n = n >> 1
            else:
                n = n >> 1
        return count