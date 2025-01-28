// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        # To store the curr Fibonacci number
        curr = 0

        # To store the previous Fibonacci numbers
        prev1 = 1
        prev2 = 1

        # Loop to calculate Fibonacci numbers from 2 to n
        for i in range(2, n + 1):
        
            # Calculate the curr Fibonacci number
            curr = prev1 + prev2

            # Update prev2 to the last Fibonacci number
            prev2 = prev1

            # Update prev1 to the curr Fibonacci number
            prev1 = curr

        return curr