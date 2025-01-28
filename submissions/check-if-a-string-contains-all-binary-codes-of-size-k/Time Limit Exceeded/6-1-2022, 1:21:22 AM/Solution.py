// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bin_string = []
        for i in range(2**k):
            a = bin(i)[2:].zfill(k)
            if a not in s:
                return False
            continue
        return True
