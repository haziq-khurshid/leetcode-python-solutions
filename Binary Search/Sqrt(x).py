class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0,x                               # Initializing pointers at 0 and input number
        
        while left <= right:                        
            mid = left + (right-left)//2                # Find mid element  
            if mid*mid == x:                            # If square of mid element equals to input
                return mid                              # Return number as answer
            elif mid*mid > x:                           # Else If suqare is greater than input
                right = mid - 1                         # Bring right pointer to left half
            else:                                       # Else square is less than input
                left = mid + 1                          # Bring left pointet to right half
        return left-1                                   # If perfect square not found in above loop,
                                                        # return previous element of left as answer will be in points
                                                        # we need to return complete integer only
