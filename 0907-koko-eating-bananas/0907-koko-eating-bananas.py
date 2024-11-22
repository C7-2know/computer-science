class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high,low=max(piles),1
        def is_pos(tot):
            hour=0
            sum_=0
            for i in range(len(piles)):
                d=piles[i]//tot
                if piles[i]%tot!=0:
                    d+=1
                hour+=d
            return hour<=h
        min_=float('inf')
        while high>=low:
            mid=(high+low)//2
            if is_pos(mid):
                high=mid-1
                min_=min(min_,mid)
            else:
                low=mid+1
        return min_