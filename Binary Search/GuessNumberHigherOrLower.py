# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0,n                               
        
        while left <= right:                            
            mid = left + (right-left)//2                 
            if guess(mid) == 0:                     # If middle element is correct answer, return middle
                return mid
            elif guess(mid) == -1:                  # If middle element is greater than answer,
                right = mid - 1                     # Bring right pointer on left half of array
            elif guess(mid) == 1:                   # If middle element is less than answer,
                left = mid + 1                      # Bring left pointer to right half of array
        return -1               