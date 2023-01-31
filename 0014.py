class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].startswith(prefix) == False:
                if prefix == "":
                    return prefix
                prefix = prefix[:-1]
        return prefix

solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))