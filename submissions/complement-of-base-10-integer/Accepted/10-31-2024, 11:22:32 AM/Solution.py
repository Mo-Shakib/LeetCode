// https://leetcode.com/problems/complement-of-base-10-integer

class Solution(object):
    def bitwiseComplement(self, n):
	    return ((2 << int(math.log(max(n, 1), 2))) - 1) - n
        