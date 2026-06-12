class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[0 for _ in range(len(prices))]
        stack=[]
        for j in range(len(prices)):
            while stack and stack[-1][0]>=prices[j]:
                cur,i=stack.pop()
                res[i]=cur-prices[j]
                print(res)
            stack.append((prices[j],j))
        
        while stack:
            cur,i=stack.pop()
            res[i]=cur
        return res