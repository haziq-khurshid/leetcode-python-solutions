class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] < nums[right]:             # If mid element is less than right most element, right half of array is not rotated
                right = mid                         # So bring right pointer to mid
            else:
                left = mid + 1                      # Else right half is rotated so bring left to next of mid
                
        return nums[left]