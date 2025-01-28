// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        return num % 9
        