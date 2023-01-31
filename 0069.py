class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start, end = 0, x

        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                if (mid-1) * (mid-1) <= x:
                    return mid-1
                else: 
                    end = mid-1
            else:
                start = mid+1

solution = Solution()
print(solution.mySqrt(8))