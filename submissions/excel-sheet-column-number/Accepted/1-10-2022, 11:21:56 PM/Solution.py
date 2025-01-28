// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for x in range(len(columnTitle)):
            res += 26**(len(columnTitle)-x-1) * (ord(columnTitle[x]) - ord('A') + 1)
        return res
        