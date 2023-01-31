class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for i in range(numRows-1):
            row = []
            row = [1] + [ triangle[i][j] + triangle[i][j+1] for j in range(len(triangle[i])-1) ] + [1]
            triangle.append(row)
        return triangle 

solution = Solution()
print(solution.generate(5))

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]