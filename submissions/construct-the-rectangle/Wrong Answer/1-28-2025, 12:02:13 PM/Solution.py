// https://leetcode.com/problems/construct-the-rectangle

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area**0.5 == area/area**0.5:
            return [int(area**0.5), int(area**0.5)]
        i = 1
        l = 0
        w = 0
        while i*i < area:
            if area % i == 0:
                l = int(area/i)
                w = int(area/l)
            i += 1
        return [l, w]

        
        