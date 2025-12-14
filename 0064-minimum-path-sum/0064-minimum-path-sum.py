class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dc={}
        lr, lc = len(grid)-1, len(grid[0])-1
        def dp(r,c):
            
            if (r,c) in dc:
                return dc[(r,c)]
            if r==lr and c==lc:
                return grid[r][c]
            if r>lr or c> lc:
                return float("inf")
            dc[(r,c)] = grid[r][c] + min(dp(r+1,c), dp(r,c+1))
            return dc[(r,c)]
        return dp(0,0)