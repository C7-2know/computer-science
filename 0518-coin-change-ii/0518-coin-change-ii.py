class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dp(i,amt):
            if i>=len(coins) or amt<0:
                return 0
            if amt==0:
                return 1
            if (i,amt) not in memo:
                memo[(i,amt)]=dp(i+1,amt)+dp(i,amt-coins[i])
            return memo[(i,amt)]
        
        return dp(0,amount) 