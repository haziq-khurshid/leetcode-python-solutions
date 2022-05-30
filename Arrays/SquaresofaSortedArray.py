class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = sorted(list(map(lambda x:x*x, nums)))     # map() updates the list by passing
                                                        # the list as argument to the expression x*x
                                                        # Result is then sorted using sorted() function
        return res


"""Below is the function call to test above function,
   you can change input and test as well."""
def main():
    input = [-4,-1,0,3,10]              
    sol = Solution()
    ans = sol.sortedSquares(input)
    print("Output: ", ans)

if __name__ == "__main__":
    main()