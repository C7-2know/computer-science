class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_possible(mid,n,quantities):
            for i in range(len(quantities)):
                if quantities[i]%mid==0:
                    n-=quantities[i]//mid
                else:
                    n-=(quantities[i]//mid+1)
            return n>=0
        low=1
        high=max(quantities)
        min_=float("inf")
        while low<=high:
            mid=(high+low)//2
            ans= is_possible(mid,n,quantities)
            if ans:
                min_=min(mid,min_)
                high=mid-1
            else:
                low=mid+1
        return min_
