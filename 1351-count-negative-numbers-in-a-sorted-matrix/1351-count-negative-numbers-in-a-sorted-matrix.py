class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        lr, lc = len(grid), len(grid[0])
        nv = 0
        for i in range(len(grid)):
            if grid[i][0]<0:
                nv += (len(grid)-i)*len(grid[0])
                break
            j=0
            while j<lc:
                if grid[i][j]<0:
                    lc = j
                j+=1
            nv+= len(grid[0])-lc
        return nv
            