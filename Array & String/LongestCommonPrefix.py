class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = strs[0]                               # Taking first string in result
        for str in strs:
            while not str.startswith(res):          # While string doesn't matches first string,
                res = res[:-1]                      # keep removing last character of the string
        return res


"""Below is the function call to test above function,
    you can change strings in input"""
def main():
    strs = ["flower","flow","flight"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)

if __name__ == "__main__":
    main()