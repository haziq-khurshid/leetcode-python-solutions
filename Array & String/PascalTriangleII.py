class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res =[[1]]                                  # First row would always be one
        for i in range(rowIndex):                   # Range would rowIndex i.e total number of rows
            temp = [0] + res[-1] + [0]              # Append 0 on start and end of a row to calculate sum in next row
            row = []                            
            for j in range(len(res[-1])+1):         
                row.append(temp[j]+temp[j+1])       # Sum two numbers on top of current index and add answer in new row
            res.append(row)                         # Append new row in the result
        return res[rowIndex]                        # Return the row from the result which was passed in input


"""Below is the function call to test above function,
    you can change rowIndex in input"""
def main():
    rowIndex = 3
    sol = Solution()
    sol.getRow(rowIndex)
    
if __name__ == "__main__":
    main()