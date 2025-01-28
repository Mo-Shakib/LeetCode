// https://leetcode.com/problems/construct-the-rectangle

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area**0.5 == area/area**0.5:
            return [int(area**0.5), int(area**0.5)]
        res = []
        for i in range(1, int(area**0.5)):
            if area % i == 0:
                res.append([(area//i), i])
        return res[-1]
        
        