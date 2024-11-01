# Top K Frequent Elements
**URL**: [https://leetcode.com/problems/top-k-frequent-elements/description/](https://leetcode.com/problems/top-k-frequent-elements/description/)

**Description:**

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

 __Example 1:__
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

 __Example 2:__
```
Input: nums = [1], k = 1
Output: [1]
```

 __Constraints:__
```
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
```
Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
@lc code=start

**Solution Code**:
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        # Sort the dictionary based on values and create a list of keys
        sorted_keys = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)

        return sorted_keys[:k]

```
