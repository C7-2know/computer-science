class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo={}
        def dp(i,st):
            if i>=len(prices):
                return 0
            if (i,st) not in memo:
                if st=="b":
                    memo[(i,st)]=max(dp(i+1,"s")-prices[i],dp(i+1,"b"))
                if st=="s":
                    memo[(i,st)]=max(dp(i+1,"b")+prices[i]-fee,dp(i+1,"s"))
            return memo[(i,st)]
        return dp(0,"b")