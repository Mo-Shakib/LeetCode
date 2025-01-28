// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I' : 1,
            'V': 5,
            'X': 10,
            'L':50,
            'C': 100,
            'D':500,
            'M':1000
        }
        digit = []
        res = 0
        for char in s:
            digit.append(vals[char])
        
        digit.append(0)
        for i in range(len(digit)-1):
            if digit[i] >= digit[i+1]:
                res += digit[i]
            else:
                res -= digit[i]

        return res

