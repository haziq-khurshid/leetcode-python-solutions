class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0                     
        second = 1
        for _ in range(n):
            first ,second = second, first+ second    # Update second by adding both, update first to previous second
        return second                                # return answer
        
        """
        Memoization Solution
        cache = {}                              # Avoid calculating answers again
        def rec(n):                             
            if n in cache: return cache[n]      # If n in cache, return answer
            if n <= 2: return n
            cache[n] = rec(n-1) + rec(n-2)      # Call recursive method for preivous two answers
            return cache[n]                     
        return rec(n)
        """