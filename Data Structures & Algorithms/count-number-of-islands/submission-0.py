class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols = len(grid), len(grid[0])

        def markIsland(r,c):

            if (r <0 or r >= rows) or (c < 0 or c>= cols) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr,dc in ([0,1], [0,-1], [-1,0], [1,0]):
                markIsland(r + dr,c + dc)
        
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res+= 1
                    markIsland(i,j)
        
        return res