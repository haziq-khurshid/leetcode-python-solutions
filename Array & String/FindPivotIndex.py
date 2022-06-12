class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)                                   # Total sum of nums
        left_sum = 0                                            # Left sum to be set to zero in start
        for index, value in enumerate(nums):
            if left_sum == total_sum - left_sum - value:        # If sum on left side of an index is equal to sum on right side
                return index                                    # Return current index as answer
            else:
                left_sum+=value                                 # Else add current number in left sum
        return -1                                               # If pivot index is not found, return -1

"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [1,7,3,6,5,6]
    sol = Solution()
    result = sol.pivotIndex(nums)
    print(result)

if __name__ == "__main__":
    main()