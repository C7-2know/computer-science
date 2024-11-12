class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo={}
        def dp(l,r):
            if abs(l-r)<=1:
                return 0
            if (l,r) not in memo:
                ans=float('inf')
                for i in range(l+1,r):
                    ans=min(ans,dp(l,i)+dp(i,r)+values[i]*values[l]*values[r])
                memo[(l,r)]=ans
            return memo[(l,r)]
        return dp(0,len(values)-1)