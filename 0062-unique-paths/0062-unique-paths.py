class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo={}
        # def dp(r,c):
        #     if r>=m or c>=n:
        #         return 0
        #     if r==m-1 and c==n-1:
        #         return 1
        #     if (r,c) not in memo:
        #         memo[(r,c)]= dp(r+1,c)+dp(r,c+1)
        #     return memo[(r,c)]
        # return dp(0,0)
        arr=[[0 for _ in range(n)]for _ in range(m)]
        arr[m-1][n-1]=1
        # arr[m-2][n-1]=1
        # print(arr)
        direction=[(0,1),(1,0)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                path=0
                for rc,cc in direction:
                    nr,nc=rc+i,cc+j
                    if nr<m and nc<n:
                        path+=arr[nr][nc]
                if path!=0:
                    arr[i][j]=path
            
        return arr[0][0]
