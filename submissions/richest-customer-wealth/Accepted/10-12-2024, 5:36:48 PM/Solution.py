// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = []
        for w in accounts:
            max_w.append(sum(w))
        return max(max_w)
        