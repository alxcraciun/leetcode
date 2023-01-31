class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        while n: 
            a, b = b, a+b
            n -= 1
        return b

'''
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''