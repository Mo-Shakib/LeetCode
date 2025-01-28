// https://leetcode.com/problems/pascals-triangle



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
        