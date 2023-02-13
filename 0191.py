'''
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Input: n = 00000000000000000000000000001011
Output: 3

Input: n = 00000000000000000000000010000000
Output: 1

Input: n = 11111111111111111111111111111101
Output: 31

The input must be a binary string of length 32.
Follow up: If this function is called many times, how would you optimize it?
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0 
        for _ in range(32):
            if n & 1 == 1:
                counter += 1
            n >>= 1
        return counter

solution = Solution().hammingWeight(0b00000000000000000000000000001011)
print(solution)