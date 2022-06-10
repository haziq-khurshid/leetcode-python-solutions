class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even_nums,odd_nums = [],[]                  # Initializing empty arrays for even & odd numbers
        for i in range(len(nums)):                  
            if nums[i] % 2 == 0:                    # If number is even, add it to even array
                even_nums.append(nums[i])
            else:                                   # If number is odd, add it to odd array
                odd_nums.append(nums[i])
        return even_nums + odd_nums                 # Return both arrays together

    """ Below is the function call to test above function, you can change nums in input """
def main():
    nums = [1,2,4,5,7]
    sol = Solution()
    sol.sortArrayByParity(nums)
    
if __name__ == "__main__":
    main()