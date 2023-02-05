'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
n == nums.length
1 <= n <= 5 * 10**4
-10**9 <= nums[i] <= 10**9
'''

# Boyer-Moore Algorithm for Voting
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = 0
        candidate = None

        for elem in nums:
            if counter == 0:
                candidate = elem

            if elem == candidate:
                counter += 1
            else:
                counter -= 1
        return candidate