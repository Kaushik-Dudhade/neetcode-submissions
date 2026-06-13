from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0
        rows,cols = len(grid), len(grid[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        if not fresh:
            return 0
        
        mins = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in ([1,0],[-1,0], [0,1], [0,-1]):
                    if 0<=r+dr<rows and 0 <= c+dc<cols:
                        if grid[r+dr][c+dc] == 1:
                            grid[r+dr][c+dc] = 2
                            fresh -=1

                            q.append((r+dr,c+dc))
        
            mins += 1
        
        if fresh:
            return -1
        
        return  mins


