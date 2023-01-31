# Max Sum

# Brute Force
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


# Dictionary Optimised
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_index = {}
        for i in range(len(nums)):   
            if target - nums[i] not in dict_index:
                dict_index[target-nums[i]] = i
            else:
                return [i, dict_index[nums[i]]]
            


nums1 = [2,7,11,15]
target1 = 9

nums2 =  [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

print(Solution2().twoSum(nums1, target1))
