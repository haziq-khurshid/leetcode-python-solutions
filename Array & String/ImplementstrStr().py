class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0                           # Return 0 if needle is empty string
        length = len(needle)                                # Take length of needle
        for i in range(len(haystack) - length + 1):         # Remove length of needle from traversal & add 1 because we will be searching whole needle
                                                            # If needle isn't found at "length of haystack - length of needle", needle won't be found    
            if haystack[i:i+length] == needle:
                return i                                    # Return position of needle found
        return -1                                           # Return -1 if needle not found



"""Below is the function call to test above function,
    you can change strings in input"""
def main():
    haystack = "hello"
    needle = "ll"
    sol = Solution()
    result = sol.strStr(haystack,needle)
    print(result)

if __name__ == "__main__":
    main()