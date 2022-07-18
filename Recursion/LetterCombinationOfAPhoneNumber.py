class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Dict to track digits to characters
        digitToChar = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}
        # Recursive function to backtrack
        def backtrack(i, currStr):
            if len(currStr) == len(digits):           # When length of current string matches length of input digits,
                res.append(currStr)                   # Append current combination to result and return
                return
            for c in digitToChar[digits[i]]:          # Run loop for each character mapped to the digit
                backtrack(i+1 ,currStr+c)             # Call recursive function for next digit by appending current character to currStr
           
        res = []            
        if digits:                                    # If input is not empty, call recursive funciton
            backtrack(0, '')
        return res