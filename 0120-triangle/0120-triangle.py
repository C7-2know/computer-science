class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[0 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))] 
        dp[0][0]=triangle[0][0]
        def is_valid(i,j):
            return i>=0 and j>=0 and j<len(triangle[i])

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                pre1,pre2=float('inf'),float('inf')
                if is_valid(i-1,j-1):
                    pre1=dp[i-1][j-1]
                if is_valid(i-1,j):
                    pre2=dp[i-1][j]
                
                dp[i][j]=min(pre1,pre2)+triangle[i][j]
        # print(dp)
        return min(dp[-1])