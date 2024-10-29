# Running Sum of 1d Array
**URL**: [https://leetcode.com/problems/running-sum-of-1d-array/description/](https://leetcode.com/problems/running-sum-of-1d-array/description/)

**Description**
Given an array nums. We define a running sum of an array as runningSum[i] =
sum(nums[0]…nums[i]).
Return the running sum of nums.

 __Example 1:__
```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

 __Example 2:__
```
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1,
1+1+1+1+1].
```

 __Example 3:__
```
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

 __Constraints:__
```
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
```

**Solution Code**:
```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = nums[:1]
        for i in range(1, len(nums)):
            res.append((res[-1] + nums[i]))
        return res
```
