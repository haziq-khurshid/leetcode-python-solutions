class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0                     # If base is 0, return 0
        def pow(x,n):                           # Helper function for recursion
            if n == 0: return 1                 # If exponenet is 0, return 1
            res = pow(x, n//2)                  # Using divide and conquer, find answer for half of exxponent
            if n % 2 == 0:                      # If exp is even, multiply half answer with itself to get answer
                return res * res
            else:
                return x * (res * res)          # If exp is odd, multiply half with itself and then with base to get answer
             
        res = pow(x, abs(n))                    # Pass positive number as exponene
        return res if n >=0 else 1/res          # If exponent was negative, divide 1/result, else return result