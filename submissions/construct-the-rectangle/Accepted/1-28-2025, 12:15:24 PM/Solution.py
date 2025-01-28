// https://leetcode.com/problems/construct-the-rectangle

import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = 1
        l = 0
        w = 0
        while math.floor(i*i) <= area:
            if area % i == 0:
                w = i
                l = area/w
            i += 1
        return [int(l), int(w)]

        
        