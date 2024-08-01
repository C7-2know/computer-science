class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo={}
        n,m=len(dungeon),len(dungeon[0])
        def is_valid(r,c):
            return r>=0 and r<n and c>=0 and c<m
        dp=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        if dungeon[n-1][m-1]<0:
            dp[n-1][m-1]=abs(dungeon[n-1][m-1])
        else:
            dp[n-1][m-1]=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:
                    continue
                down,right=float('inf'),float('inf')
                if is_valid(i+1,j):
                    down=dp[i+1][j]
                if is_valid(i,j+1):
                    right=dp[i][j+1]
                nd=min(right,down)
                if nd>0 and dungeon[i][j]>0:
                    nd-=dungeon[i][j]
                    if nd<0:
                        nd=0
                elif dungeon[i][j]<0:
                    nd+=abs(dungeon[i][j])
                # elif dungeon[i][j]==0:
                #     nd+=1
                dp[i][j]=nd
                # print(i,j,nd,down,right)

                # print(dp)
        
        return dp[0][0]+1 if dp[0][0]!=float('inf') else 0
