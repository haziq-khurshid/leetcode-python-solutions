class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left , right = 0 , len(nums)-1
        
        while left < right:
            middle = left + (right - left) //2
            if nums[middle] > nums[middle+1]:        # If mid element is greater than its next, it is one of peaks
                right = middle                       # Bring right pointer back to middle
            else:
                left = middle + 1                    # If mid element is equal or less than next element, its not a peak
        return left                                  # Move left pointer forward