// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n==1):
            return True
        
        n_bin = bin(n)
        n_bin = n_bin[2:]
        
        if (n_bin[0]!= '1'):
            return False
        
        elif (n_bin.count('1')>1):
            return False
        
        return True
                