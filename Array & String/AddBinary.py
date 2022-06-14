class Solution:
    def addBinary(self, a: str, b: str) -> str:    
        first = int(a,2)                    # Converting to decimal from base 2
        second = int(b,2)                   # Converting to decimal from base 2
        res = bin(first+second)             # Adding both numbers in decimal
        return res[2:]                      # Returning answer from 3rd index as first two indices are '0b'

"""Below is the function call to test above function,
    you can change strings in input"""
def main():
    a = "11"
    b = "1"
    sol = Solution()
    result = sol.addBinary(a,b)
    print(result)

if __name__ == "__main__":
    main()