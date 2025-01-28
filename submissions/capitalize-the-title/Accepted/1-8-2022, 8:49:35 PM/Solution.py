// https://leetcode.com/problems/capitalize-the-title

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        res = ""
        for char in title:
            if 1 <= len(char) <= 2:
                res += char.lower()
            else:
                res += char[0].upper() + char[1:].lower()
            res += " "
        return res[:-1]