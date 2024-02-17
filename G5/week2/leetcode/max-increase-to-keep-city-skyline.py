class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        colums=[]
        for i in range(len(grid)):
            colums.append([])
            for j in range(len(grid)):
                colums[i].append(grid[j][i])
        # print(colums)
        max_r=[]
        max_c=[]
        for i in range(len(grid)):
            max_r.append(max(grid[i]))
            max_c.append(max(colums[i]))
        # print(max_r,max_c)
        inc=0
        for r in range(len(grid)):
            for c in range(len(grid)):
                inc+=(min(max_r[r],max_c[c])-grid[r][c])  
        return inc