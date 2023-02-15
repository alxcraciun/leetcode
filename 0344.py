'''
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory, do not return the string.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
1 <= s.length <= 105
s[i] is a printable ascii character.
'''

class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Built-in Method in Python
        # s.reverse()
        a = len(s) // 2
        b = len(s) - 1
        for i in range(0, a):
            s[i], s[b] = s[b], s[i]
            b -= 1

s = ["h", "e", "x", "l", "o"]
Solution().reverseString(s)
print(s)
