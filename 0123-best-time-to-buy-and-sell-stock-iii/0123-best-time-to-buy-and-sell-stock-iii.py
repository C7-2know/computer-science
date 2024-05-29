class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dp(i,st,t):
            if i>=len(prices) or t == 0:
                # if st=='b':
                #     return float('-inf')
                return 0
            if (i,st,t) not in memo:
                if st=='b':
                    memo[(i,st,t)]=max(dp(i+1,'b',t),dp(i+1,"s",t)-prices[i])
                if st=="s":
                    memo[(i,st,t)]=max(dp(i+1,"s",t),dp(i+1,'b',t - 1)+prices[i])
                
            return memo[(i,st,t)]
        return dp(0,"b",2)