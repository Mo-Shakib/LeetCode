// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            if len(set(matrix[i])) != n:
                return False
        for j in range(n):
            temp = []
            for i in range(n):
                temp.append(matrix[i][j])
            if len(set(temp)) != n:
                return False
        return True