class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0                           # Initializing start & end pointers
        end = len(numbers)-1
        while start < end:                      
            sum = numbers[start] + numbers[end]     
            if sum == target:               # If sum = target, we are at correct indices
                return (start+1,end+1)
            elif sum < target:              # If sum < target, we need to increase sum, so move start step ahead
                start+=1
            else:                           # If sum > target, we need to decrease sum, so move end step back
                end-=1
            
"""Below is the function call to test above function,
    you can change numbers and target in input"""
def main():
    numbers = [1,2,4,6]
    target = 5
    sol = Solution()
    res = sol.twoSum(numbers , target)
    print(res)
if __name__ == "__main__":
    main()