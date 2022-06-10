class Solution:
    def moveZeroes(self, nums: list[int]) -> int:
        count = 0                            # Keep count of non-zero elements
        n = len(nums)                        # Length of array
        for i in range(n):                     
            if nums[i] != 0:                 # If number is non-zero
                nums[count] = nums[i]        # Start placing it based on non-zero count in array
                count+=1                     # Increase count of non-zero elements

        for i in range(count,n):             # Difference between length of array and count is number of zeroes
            nums[i] = 0                      # Keep placing zeroes based on the difference
            
"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [0,1,0,3,12]
    sol = Solution()
    sol.moveZeroes(nums)
    
if __name__ == "__main__":
    main()