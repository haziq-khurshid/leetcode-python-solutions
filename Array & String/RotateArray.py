class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)                                           # Taking mod so if k > length of nums, we rotate correctly
        def reverse(nums,left,right):                               # Creating a reverse function to call multiple times
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        
        reverse(nums,left = 0 , right = len(nums)-1)                # Reversing original numbers
        reverse(nums,left = 0, right = k - 1)                       # Reversing numbers on left side of k
        reverse(nums,left = k, right = len(nums)-1)                 # Reversing numbers on right side of k

"""Below is the function call to test above function,
    you can change numbers and k steps in input"""
def main():
    nums = [1,2,4,6]
    k = 2
    sol = Solution()
    sol.rotate(nums, k)
    
if __name__ == "__main__":
    main()