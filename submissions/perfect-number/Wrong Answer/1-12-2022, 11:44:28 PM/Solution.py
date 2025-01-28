// https://leetcode.com/problems/perfect-number

import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [1]
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                divisors.extend([i,num/i])
                
        if sum(set(divisors)) == num:
            return True
        return False
    
        