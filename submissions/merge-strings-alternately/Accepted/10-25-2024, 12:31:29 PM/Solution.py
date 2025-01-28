// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        m = min(len1, len2)

        res = ''

        for i in range(m):
            res += word1[i] + word2[i]

        if len1 == len2:
            return res
        elif m == len1:
            return res + word2[m:]
        else:
            return res + word1[m:]