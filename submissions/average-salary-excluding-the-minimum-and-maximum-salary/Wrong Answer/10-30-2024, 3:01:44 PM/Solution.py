// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

class Solution:
    def average(self, salary: List[int]) -> float:
        return (min(salary) + max(salary))/2
        