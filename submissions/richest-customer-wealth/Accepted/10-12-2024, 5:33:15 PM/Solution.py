// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = 0
        for w in accounts:
            if sum(w) > max_w:
                max_w = sum(w)
        return max_w
        