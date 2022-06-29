class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0                         # Fibonacci of 0 is 0
        if n == 1: return 1                         # Fibonacci of 1 is 1
        ans = self.fib(n - 1) + self.fib(n - 2)     # Call recursive method for n-1 & n-2, add the sum as answer
        return ans