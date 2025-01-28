// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        lenth = len(matrix[0])
        for i in matrix:
            if len(set(i)) != lenth:
                return False
        return True