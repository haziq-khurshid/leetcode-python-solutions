class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left,total = 0,0                                # Initializing left pointer at start & total equal to zero
        res = len(nums)+1                               # Taking result as length + 1 because we will be using minimum later to reduce it

        for right in range(len(nums)):                  # Traverse through list using right pointer
            total+= nums[right]                         # Add current value to total
            while total >= target:                      # While current total equals or exceeds target
                res= min(res, right - left + 1)         # Take minimum of previous result and current window size as new result
                total-=nums[left]                       # Remove left value from total
                left+=1                                 # Take left pointer a step ahead
        return res if res != len(nums)+1 else 0         # Return result if minimum subarray was found else return 0

"""Below is the function call to test above function,
    you can change numbers and target in input"""
def main():
    numbers = [1,2,4,6]
    target = 10
    sol = Solution()
    res = sol.minSubArrayLen(target, numbers)
    print(res)
if __name__ == "__main__":
    main()