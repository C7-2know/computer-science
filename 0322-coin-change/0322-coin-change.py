class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo=[amount+1]*(amount+1)
        # memo[0]=0
        # for i in range(1,amount+1):
        #     for coin in coins:
        #         if i-coin>=0:
        #             memo[i]=min(memo[i],1+memo[i-coin])
        #     # print(memo)
        # return memo[amount] if memo[amount]!=amount+1 else -1
        
        memo={}
        def dp(i,amt):
            if i>=len(coins) or amt<0:
                return float('inf')
            if amt==0:
                return 0
            if (i,amt) not in memo:
                memo[(i,amt)]=min(dp(i,amt-coins[i])+1,dp(i+1,amt))
            return memo[i,amt]
        res=dp(0,amount)
        if res==float("inf"):
            return -1
        return res
        # coins.sort(reverse=True)
        # if amount==0:
        #     return 0
        # memo={i:float("inf") for i in range(len(coins))}
        # def dp(i,amt):
        #     print(amt)
        #     if sum(amt)>amount:
        #         return float('inf')
        #     if sum(amt)==amount:
        #         print(amt)
        #         return len(amt)
        #     if i>=len(coins):
        #         return float('inf')
        #     if i not in memo:
        #         memo[i]=min(dp(i,amt+[coins[i]]),dp(i+1,amt))
        #     return memo[i]
        # min_=float('inf')
        # print(memo)
        # for i in range(len(coins)):
        #     min_=min(min_,dp(i,[]))
        # if min_==float('inf'):
        #     return -1       
        # return min_