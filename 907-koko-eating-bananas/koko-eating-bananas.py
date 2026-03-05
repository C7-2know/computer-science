class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(k,h):
            for i in piles[::-1]:
                if i>=k:
                    h-=(i//k)
                    if i%k!=0:
                        h-=1
                else:
                    h-=1
                if h<0:
                    return False
            return True
        low,max_=1,max(piles)
        while low<max_:
            mid=(max_+low)//2
            if is_possible(mid,h):
                max_=mid
            else:
                low=mid+1
        return max_
        