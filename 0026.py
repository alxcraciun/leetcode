class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        unique = 0
        last_number = None
        for elem in nums:
            if elem == last_number:
                continue
            else:
                nums[unique] = elem
                last_number = elem
                unique += 1
        return unique

solution = Solution()
print(solution.removeDuplicates([[1,1,2]]))

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]
                l += 1
        return l
'''