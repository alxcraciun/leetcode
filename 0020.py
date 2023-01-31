class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for par in s:
            if par == '(' or par == '[' or par == '{':
                opened.append(par)
            else:
                if not opened:
                    return False
                last = opened.pop()
                if par == ')' and last != '(':
                    return False
                elif par == ']' and last != '[':
                    return False
                elif par == '}' and last != '{':
                    return False
        return opened == []
