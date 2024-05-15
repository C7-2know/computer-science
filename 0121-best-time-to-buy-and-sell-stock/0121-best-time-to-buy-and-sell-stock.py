class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dp(i):
            if i>=len(prices):
                return 0
            if i not in memo:
                memo[i]= max(dp(i+1),prices[i])
            return memo[i]
        max_=0
        for i in range(len(prices)-1):
            max_=max(max_,dp(i+1)-prices[i])
        return max_