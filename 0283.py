''' 283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array. Do not return anything, modify nums in-place instead.

Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Input: nums = [0]
Output: [0]

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)