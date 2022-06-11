class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))          # Removing Duplicates from the list
        nums = sorted(nums)             # Sorting the list
        if len(nums) < 3:               # If length less than 2, return maximum number
            return nums[-1]
        else:                           # Else length is greater than 3, return third maximum number
            return nums[-3]             
        
"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [1,-1,2,4,5,3]
    sol = Solution()
    max = sol.thirdMax(nums)
    print(max)

if __name__ == "__main__":
    main()