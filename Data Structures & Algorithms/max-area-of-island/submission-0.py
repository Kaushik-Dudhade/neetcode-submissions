class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])

        def dfs(r,c):
            
            if (r < 0 or r >= rows) or ( c < 0 or c >= cols) or grid[r][c] == 0:
                return 0
            
            cur_size = 1

            grid[r][c] = 0

            for dr,dc in ([1,0],[-1,0], [0,1],[0,-1]):
                cur_size += dfs(r+dr,c+dc)
            
            return cur_size
        
        max_size = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i,j))
        
        return max_size


            