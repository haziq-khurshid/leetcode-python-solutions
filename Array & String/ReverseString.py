class Solution:
    def reverseString(self, s: list[str]) -> None:
        start = 0                                        # Pointer at start
        end = len(s) - 1                                 # Pointer at end   
        while start <= end:                              # While start pointer doesn't cross end pointer
            s[start], s[end] = s[end],s[start]           # Swap values at both pointers
            end -= 1                                     # Bring end pointer a step back
            start += 1                                   # Take start pointer a step ahead

"""Below is the function call to test above function,
    you can change string in input"""
def main():
    s = ["h","e","l","l","o"]
    sol = Solution()
    sol.reverseString(s)
    
if __name__ == "__main__":
    main()