class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0                         # Return 0 at first level
        parent = self.kthGrammar(n-1,(k+1)//2)      # Call recursive method to find parent of current index
                                                    # Odd indices will have same value as parent index, even have opposite
        if k % 2 == 0:                              
            return 0 if parent else 1               # If index is even, return opposite of parent 
        else:
            return 1 if parent else 0               # If index is odd, return same of parent