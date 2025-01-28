// https://leetcode.com/problems/top-k-frequent-elements

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
        