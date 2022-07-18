# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left , right = 1 , n                                
        while left < right:
            middle = left + (right - left) //2
            if isBadVersion(middle):                  # If bad version is found, bring right pointet to it, as it is a possible answer
                right = middle                        # and numbers ahead of it doesn't matter
            else:
                left = middle + 1                     # If bad version isn't found in middle, ignore first half and bring left pointer ahead
        return left
        