class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()                     # Sorting list
        return sum(nums[::2])           # Take sum of nums after skipping adjacent numbers from sorted list to maximize output
                                              
"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [1,4,3,2]
    sol = Solution()
    sol.arrayPairSum(nums)
    
if __name__ == "__main__":
    main()