// https://leetcode.com/problems/perfect-number

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
        return False
    
        