class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)                   # Getting length of array
        count , res = 0,0               # Count & Result variables declared for later use
        for i in range(0,n):            
            if nums[i] == 0:            # Set count to 0 when find a Zero in array
                count=0
            else:
                count+=1                # Increase count when find a One in array
                res = max(count,res)    # Result would be maximum of current count versus previous result
        return res


"""Below is the function call to test above function,
   you can change input & expected output and test as well."""
def main():
    input = [1,1,0,1,1,1]              # number should be either 0 or 1
    sol = Solution()
    ans = sol.findMaxConsecutiveOnes(input)
    print("Expected output: 3")
    print("Your output: ", ans)

if __name__ == "__main__":
    main()