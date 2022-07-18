class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:                                     # If target is at mid, return mid
                return mid
            # Either left or right side of mid will be sorted correctly
            # If left element is less or equal to mid, it means it is in increasing order,
            # Thus Left Sorted Portion                           
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:           # If target not part of left sorted portion,
                    left = mid + 1                                      # Move left pointer on right half of array
                else:
                    right = mid -1                                      # Else bring right pointer to left half of array
            
            # Else Right Sorted Portion
            else:
                if target < nums[mid] or target > nums[right]:          # If target not part of right sorted portion,
                    right = mid - 1                                     # Bring right pointer to left half of array
                else:
                    left = mid + 1                                      # Else move left pointer to right half of array
        return -1