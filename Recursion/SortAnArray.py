class Solution:
    # Sorting using Merge Sort ( Divide & Conquer)
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):                             # Merge method to merge left and right side
            res = []
            while left and right:                          # While both sides are not empty
                if left[0] <= right[0]:                    # If left has smaller value, add it to result
                    res.append(left.pop(0))
                else:                                      # If right has smaller value, add it to result                
                    res.append(right.pop(0))
            res = res + left + right                        # When either side is empty, add remaining to result
            return res
        
        n = len(nums)                                   
        if n == 1: return nums              
        left_sorted = self.sortArray(nums[:n//2])           # Calling recursive method for left half of list
        right_sorted = self.sortArray(nums[n//2:])          # Calling recursive method for right half of list
        
        return merge(left_sorted,right_sorted)              # Call merge method to merge both sides