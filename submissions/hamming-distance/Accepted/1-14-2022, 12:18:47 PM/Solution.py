// https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = bin(x ^ y)[2:]
        return str(res).count('1')
        