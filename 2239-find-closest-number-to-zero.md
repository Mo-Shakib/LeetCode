# Find Closest Number to Zero
**URL**: [https://leetcode.com/problems/find-closest-number-to-zero/description/](https://leetcode.com/problems/find-closest-number-to-zero/description/)

**Description**
the largest value.

 __Example 1:__
```
Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
```

 __Example 2:__
```
Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is
returned.
```

 __Constraints:__
```
1 <= n <= 1000
-10^5 <= nums[i] <= 10^5
```

**Solution Code**:
```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')
        nums = set(nums)
        for i in nums:
            if abs(i) < abs(res):
                res = i
            elif i == abs(res):
                if i > res:
                    res = i
        return res

```
