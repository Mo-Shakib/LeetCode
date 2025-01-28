// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the smallest length element
        smallest_length_element = min(strs, key=len)
        # Get the length of the smallest element
        smallest_length = len(smallest_length_element)
        res = ''
        for i in range(smallest_length):
            x = len(strs)
            y = 0
            for element in strs:
                if element[i] == smallest_length_element[i]:
                    y += 1
                    if y == x:
                        res += element[i]
                        y = 0
                else:
                    return res
        return res

        