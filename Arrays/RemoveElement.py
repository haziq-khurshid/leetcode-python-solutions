class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0                                   # Variable to count numbers other than the value to be removed
        for i in range(len(nums)):
            if nums[i] != val:                      # In case number doesn't macth the value,
                nums[count] = nums[i]               # start placing it from start of array
                count +=1                           # Take pointer to next step
                                                    # Don't move pointer if number matches the value
        return count

"""Below is the function call to test above function,
    you can changes nums & val to removed in input"""
def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    count = sol.removeElement(nums,val)
    print(count, nums[:count])

if __name__ == "__main__":
    main()