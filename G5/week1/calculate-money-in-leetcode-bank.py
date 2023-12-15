class Solution:
    def totalMoney(self, n: int) -> int:
        total=0
        week=1
        week_sum=0
        while n>0:
            if n>=7:
                week_sum=7*(2*week+6)/2
            else:
                week_sum=n*(2*week+n-1)/2
            n-=7
            total+=week_sum
            week+=1
        return int(total)
