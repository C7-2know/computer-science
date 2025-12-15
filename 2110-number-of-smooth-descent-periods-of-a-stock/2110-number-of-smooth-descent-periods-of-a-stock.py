class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descents =[]
        tot= len(prices)
        i = 0
        while i < len(prices):
            prev = prices[i]
            ln=1
            i+=1
            while i < len(prices) and prev-1 == prices[i]:
                prev=prices[i]
                i+=1
                ln+=1
            if ln>1:
                descents.append(ln)
            
        memo = {}
        for d in descents:
            if d in memo:
                tot+=memo[d]
            else:
                res=0
                for i in range(d):
                    res+=i
                memo[d]=res
                tot+=res
        return tot

            