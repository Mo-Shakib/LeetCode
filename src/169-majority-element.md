# Majority Element
**URL**: [https://leetcode.com/problems/majority-element/description/](https://leetcode.com/problems/majority-element/description/)

**Description:**

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You
may assume that the majority element always exists in the array.

 __Example 1:__
```
Input: nums = [3,2,3]
Output: 3
```

 __Example 2:__
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

 __Constraints:__
```
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
Follow-up: Could you solve the problem in linear time and in O(1) space?
```

**Solution Code**:
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]

```
