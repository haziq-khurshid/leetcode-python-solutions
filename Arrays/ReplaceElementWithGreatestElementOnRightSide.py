class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans = []
        for i in range(n - 1):                  # Run loop till second last element of array
            max_num = max(arr[i+1:])            # Find max of all numbers on righ side
            ans.append(max_num)                 # Add max number to ans array
        ans.append(-1)                          # Append -1 as last number as required
        return ans

"""Below is the function call to test above function,
    you can change arr in input"""
def main():
    arr = [17,18,5,4,6,1]
    sol = Solution()
    result = sol.replaceElements(arr)
    print(result)

if __name__ == "__main__":
    main()