class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_num = 0                                                     
        if len(nums) == 1: return 0                             # If there is one number, return 0
        for i in range(len(nums)):
            if nums[i] > max_num:                               # First find maximum number with its index
                max_num = nums[i]
                max_index = i
        for i in range(len(nums)):
            if i != max_index and nums[i]*2  > max_num:         # For indices other than max index, check if double of num is greater than max num
                return -1                                       # If found, return -1
                
        return max_index                                        # Retun max index if its greater than double of other numbers

"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [1,2,4,13,3,6,5,6]
    sol = Solution()
    result = sol.dominantIndex(nums)
    print(result)

if __name__ == "__main__":
    main()