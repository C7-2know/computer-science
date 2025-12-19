class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def is_pos(r,c):
            return r>=0 and c>=0 and r<len(grid) and c<len(grid[0])
        start = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r==0 or r==len(grid)-1 or c==0 or c==len(grid[0])-1:
                    if grid[r][c] == 1:
                        start.append((r,c))

        direction=[(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        while start:
            cur = start.pop()
            next_= []
            r,c = cur
            visited.add(cur)
            for x,y in direction:
                nr, nc = r+x, c+y
                if is_pos(nr, nc) and grid[nr][nc] != 0 and (nr,nc) not in visited:
                    next_.append((nr,nc))
            grid[r][c] = "F"
            start.extend(next_)   
            
        count =0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count+=1
        return count


