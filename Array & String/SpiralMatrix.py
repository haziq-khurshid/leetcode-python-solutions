class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0 , len(matrix[0])                # Left & Right pointers for columns
        top, bottom = 0, len(matrix)                    # Top & Bottom pointers for rows
        
        while left < right and top < bottom:            
            # Get all elements in top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            # Get all elements in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right-=1

            if not(left < right and top < bottom):
                break

            # Get all elements in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom-=1

            # Get all elements in left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left+=1
        
        return res

"""Below is the function call to test above function,
    you can change matrix in input"""
def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    result = sol.spiralOrder(matrix)
    print(result)

if __name__ == "__main__":
    main()