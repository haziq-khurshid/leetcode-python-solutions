class Solution:
    def generate(self, numRows: int) -> list[list[int]]:    
        res = [[1]]                                     # First row would always be 1   

        for i in range(numRows-1):                      # Range would be total rows in input minus one
            temp = [0] + res[-1] + [0]                  # Appending 0 to both sides of most recent row, so addition could be easier in next step
            row = []                                    # Initializing an empty list for new row
            for j in range(len(res[-1])+1):             # Range would be equal to length of most recent row plus one
                row.append(temp[j]+temp[j+1])           # Add two numbers and append in the new list/row
            res.append(row)                             # Append new list/row to the result

        return res

"""Below is the function call to test above function,
    you can change numRows in input"""
def main():
    numRows = 5
    sol = Solution()
    result = sol.generate(numRows)
    print(result)

if __name__ == "__main__":
    main()