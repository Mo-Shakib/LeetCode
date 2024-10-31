# Average Salary Excluding the Minimum and Maximum Salary
**URL**: [https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/)

**Description:**

You are given an array of unique integers salary where salary[i] is the
salary of the i^th employee.
Return the average salary of employees excluding the minimum and maximum
salary. Answers within 10^-5 of the actual answer will be accepted.

 __Example 1:__
```
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000
respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 =
2500
```

 __Example 2:__
```
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000
respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
```

 __Constraints:__
```
3 <= salary.length <= 100
1000 <= salary[i] <= 10^6
All the integers of salary are unique.
```

**Solution Code**:
```python
class Solution:
    def average(self, salary: List[int]) -> float:
        return ((sum(salary)- max(salary) - min(salary))/ (len(salary)-2) )

```
