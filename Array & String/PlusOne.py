class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))           # Converting list to a number e.g. [1,2,3] => 1*(pow(10,2)) + 2*(pow(10,1)) + 3*(pow(10,0)) => 123
        return list(map(lambda x : int(x),str(num+1)))              # Converting integer plus 1 to string, so it can be mapped to list
        
"""Below is the function call to test above function,
    you can change digits in input"""
def main():
    digits = [1,2,3]
    sol = Solution()
    result = sol.plusOne(digits)
    print(result)

if __name__ == "__main__":
    main()