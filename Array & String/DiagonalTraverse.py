import collections

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        res = []                                         
        dict = collections.defaultdict(list)                     # Dictionary to store matrix
        if not mat: return res                                   # Return empty result if matrix is empty
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                dict[i+j+1].append(mat[i][j])                    # Storing dictionary after traversing diagonally
        for k in sorted(dict.keys()):
            if k%2==1: dict[k].reverse()                         # Reverse order in the odd diagonals
            res += dict[k]
        return res

"""Below is the function call to test above function,
    you can change matrix in input"""
def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    result = sol.findDiagonalOrder(matrix)
    print(result)

if __name__ == "__main__":
    main()