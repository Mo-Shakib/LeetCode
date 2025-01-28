// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        total = []
        for i in sentences:
            words = i.split()
            total.append(len(words))
        return max(total)