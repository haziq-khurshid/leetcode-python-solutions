class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 1                               # Variable to keep count of non duplicate numbers
        for i in range(1,len(nums)):            # Starting from second index because first index wouldn't be duplicate of previous
            if nums[i] != nums[i-1]:            # If number is not a duplicate of previous number
                nums[count] = nums[i]           # Add the number to the position of count
                count+=1                        # Increase count of non duplicate numbers
        return count

"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    count = sol.removeDuplicates(nums)
    print(count, nums[:count])

if __name__ == "__main__":
    main()