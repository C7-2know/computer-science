class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        val=[]
        memo={}
        def dp(i,j):
            if abs(i-j)<=1:
                return 0
            if (i,j) not in memo:
                ans=float('inf')
                for n in range(i+1,j):
                    ans=min(ans,dp(i,n)+dp(n,j)+values[i]*values[j]*values[n])
                memo[(i,j)]=ans
            return memo[(i,j)]
        ans=dp(0,len(values)-1)
        return ans
