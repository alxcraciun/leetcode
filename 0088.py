class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n > 0:
            while n > 0:
                nums1[n-1] = nums2[n-1]
                n -= 1

solution = Solution()

nums1 = [0]
nums2 = [1]
m = 0
n = 1

solution.merge(nums1, m, nums2, n)
print(nums1)


''' V2 - Working 80ms / 14Mb
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0: 
            return

        i = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while i >= 0:
            if p2 == -1:
                break

            elif p1 == -1:
                nums1[i] = nums2[p2]
                p2 -= 1 
                i -= 1

            elif nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
                i -= 1

            elif nums2[p2] >= nums1[p1]:
                nums1[i] = nums2[p2]
                p2 -= 1 
                i -= 1
'''


''' V1 - not working
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = j = 0
        while i < m+n:
            if n == 0: 
                break
            elif i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i += 1
            else:
                i += 1
'''