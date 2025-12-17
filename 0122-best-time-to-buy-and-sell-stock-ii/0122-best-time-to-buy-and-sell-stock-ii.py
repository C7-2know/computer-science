class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def profit(i, pt, prev):
            if i >= len(prices):
                return pt
            
            if i in memo:
                return memo[i]
            
            buy_= profit(i+1, pt, prices[i])
            if prev != -1:
                sell_= pt+ prices[i]-prev + profit(i+1,0,-1)
                buy_= max(buy_, sell_)
            skip = profit(i+1, pt, prev)
            memo[i] = max(buy_, skip)
            return memo[i]
        profit(0,0,-1)
        return max(memo.values())