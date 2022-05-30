class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        index = 0
        while index < len(arr):
            if arr[index] == 0:                 # When a Zero is found in the list
                index += 1                      # Take index pointer to next index
                arr.insert(index - 1, 0)        # Insert a Zero behind the index pointer
                arr.pop()                       # Pop last element of array to keep array size same
            index += 1

"""Below is the function call to test above function"""
def main():
    input = [1,0,2,3,0,4,5,0]             
    sol = Solution()
    sol.duplicateZeros(input)
    
if __name__ == "__main__":
    main()