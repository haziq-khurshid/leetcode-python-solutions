from unittest import result


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)                       # Length of input array
        nums = set(nums)                    # Removing duplicates by converting to set
        result = []                         # Initializng array to store result
        for i in range(1,n+1):              
            if i not in nums:               # If a number between "1 and length of numbers" is missing from nums, add it to result
                result.append(i)
        return result
        
"""Below is the function call to test above function,
    you can change nums in input"""
def main():
    nums = [4,3,2,7,8,2,3,1]
    sol = Solution()
    missing_nums = sol.findDisappearedNumbers(nums)
    print(missing_nums)

if __name__ == "__main__":
    main()