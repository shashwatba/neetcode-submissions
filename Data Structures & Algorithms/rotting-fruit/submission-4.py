class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rotten_coordinates = deque()
        fresh_coordinates = set()
        visited = set()
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        for a, row in enumerate(grid):
            for b, column in enumerate(row):
                if grid[a][b] == 2:
                    rotten_coordinates.append((a,b))
                    visited.add((a,b))
                if grid[a][b] == 1:
                    fresh_coordinates.add((a,b))

        if not fresh_coordinates:
            return 0

        length = 0
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        while rotten_coordinates:

            for i in range(len(rotten_coordinates)):
                r,c = rotten_coordinates.popleft()
                    
                for dr,dc in movement:
                    if min(r + dr, c + dc) < 0 or (r+dr,c+dc) in visited or (r+dr) == ROWS or (c+dc) == COLUMNS or grid[r+dr][c+dc] == 0:
                        continue
                    rotten_coordinates.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
                    fresh_coordinates.remove((r+dr,c+dc))

                    if len(fresh_coordinates) == 0:
                        return length + 1

            length += 1

        return -1





        

        

            
