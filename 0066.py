class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        else:
            digits[-1] += 1     
        return digits

'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits.count(9) == len(digits):
            digits = [1] + [0] * len(digits)
        else:
            i = len(digits) - 1
            while(digits[i]==9):
                digits[i] = 0
                i-=1
            digits[i] += 1
        return digits
'''