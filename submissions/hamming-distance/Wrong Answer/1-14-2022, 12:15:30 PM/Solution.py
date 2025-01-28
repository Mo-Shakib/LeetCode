// https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        res = int(x) ^ int(y)
        return str(res).count('1')
        