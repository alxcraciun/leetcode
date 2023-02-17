''' 268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''

# Math Solution O(n) time complexity 
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)

# Moved to functools in Python3
from functools import reduce

# Bit XOR Solution: O(n) time complexity
# We merge the nums list with a complete list
# Duplicate elements remove themselves when XOR-ed
class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, list(range(len(nums)+1)) + nums)

solution = Solution2().missingNumber([9,6,4,2,3,5,7,0,1])
print(solution)
