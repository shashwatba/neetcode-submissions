class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        if grid[0][0] == 1:
            return -1

        

        ROWS = COLUMNS = len(grid)

        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.append([0,0])

        movement = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[1,1],[-1,1],[-1,-1]]

        length = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLUMNS - 1:
                    return length
                for dr,dc, in movement:
                    if min(r+dr,c+dc) < 0 or max(r+dr,c+dc) >= ROWS or (r+dr,c+dc) in visited or grid[r+dr][c+dc] == 1:
                        continue
                    queue.append([r+dr,c+dc])
                    visited.add((r+dr,c+dc))
            length += 1

        return -1


        

        
