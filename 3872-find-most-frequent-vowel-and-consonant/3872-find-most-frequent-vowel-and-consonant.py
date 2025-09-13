class Solution:
    def maxFreqSum(self, s: str) -> int:
        vouw={'a','e','i','o','u'}
        dc={'a':0}
        cons={'b':0}
        for i in s:
            if i in vouw:
                dc[i]=dc.get(i,0)+1
            else:
                cons[i]=cons.get(i,0)+1
        return max(dc.values())+max(cons.values())
