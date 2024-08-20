class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0]*(len(matrix[0])) for i in range(len(matrix))]
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])
                elif matrix[i][j]=='1':
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) 
                ans=max(ans,dp[i][j])
        print(ans)
        return ans*ans