class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []        
        if len(nums) == 1:                                  # Base Case
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums[i]                                     # Taking ith number
            perms = self.permute(nums[:i]+nums[i+1:])       # Passing list without ith number
            for perm in perms:                              
                perm.append(n)                              # Append ith number in all permutations
            result.extend(perms)                            # Add permutations to result
        return result
        