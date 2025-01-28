// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        orders = {'I':1, 'V':2, 'X':3, 'L':4, 'C':5,'D':6,'M':7}
        total = 0
        for i in range(len(s)-1):
            roman = s[i]
            
            if orders[s[i]] >= orders[s[i+1]]:
                total += values[s[i]]
            else:
                total -= values[s[i]]

        return total+values[s[-1]]
        