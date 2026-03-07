class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def profit(i, b):
            if i>= len(prices):
                return 0
            if (i, b) not in memo:
                sell= float('-inf')
                buy = float('-inf')
                if not b:
                    sell = profit(i+2, 1)+prices[i]
                else:
                    buy = profit(i+1, 0)-prices[i]
                bs_max= max(buy, sell)
                cool = profit(i+1, b)
                memo[(i,b)] = max(bs_max, cool)
            return memo[(i,b)]
        return profit(0,1)
