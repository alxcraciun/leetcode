'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number. For example:
A -> 1
B -> 2
C -> 3
Z -> 26
AA -> 27
AB -> 28 

Input: columnTitle = "A"
Output: 1

Input: columnTitle = "AB"
Output: 28

Input: columnTitle = "ZY"
Output: 701
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0 
        order = len(columnTitle) - 1
        for letter in columnTitle:
            column += (26 ** order) * (ord(letter) - ord('A') + 1)
            order -= 1
        return column

solution = Solution().titleToNumber('ZY')
print(solution)