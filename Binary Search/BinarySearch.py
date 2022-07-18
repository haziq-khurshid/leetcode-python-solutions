class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1                 # Initialzing left & right pointer on each side
        while left <= right:                    
            middle = (left + right)//2              # Calculating mid index
            if target == nums[middle]:              # If target is found at middle, return index
                return middle
            elif target < nums[middle]:             # If target is less than middle number,
                right = middle - 1                  # Bring right pointer one step behind middle
            else:
                left = middle + 1                   # Else bring left pointer to one step ahead of middle
        return -1
        