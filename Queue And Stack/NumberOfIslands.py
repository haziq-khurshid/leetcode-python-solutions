class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0                       # Check if grid is not empty
        islands = 0 
        
        def bfs(grid,r,c):                          # Function for bfs
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
                return                              # Check if indices are in grid range and equal to 1, else return
            grid[r][c] = "#"                        # Set current index to a different value to make sure it is visited
            bfs(grid, r+1, c)                       # Call function for next next row
            bfs(grid, r-1, c)                       # Call funciton for previous row
            bfs(grid, r, c+1)                       # Call function for next column
            bfs(grid, r, c-1)                       # Call funciton for previous column

        for r in range(len(grid)):                  # Traverse through each element of Grid
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(grid,r,c)                   # If "1" is found, call bfs method and pass indices               
                    islands+=1                      # Increase island count
        return islands            