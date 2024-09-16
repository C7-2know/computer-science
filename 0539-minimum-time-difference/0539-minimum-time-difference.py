class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mint=[]
        for t in timePoints:
            h,m=map(int,t.split(':'))
            mint.append(h*60+m)
        mint.sort()
        min_=25*60
        for i in range(len(mint)-1):
            min_=min(min_,mint[i+1]-mint[i])
        min_=min(min_,24*60-mint[-1]+mint[0])

        return min_

