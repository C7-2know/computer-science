class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_,max_=max(weights),sum(weights)
        res=max_
        def possible(cap):
            ships=1
            ship=0
            for i in weights:
                if ship+i>cap:
                    ship=0
                    ships+=1
                ship+=i
            return ships<=days

        while min_<=max_:
            avg=(min_+max_)//2
            if possible(avg):
                max_=avg-1
                res=min(res,avg)
            else:
                min_=avg+1
        return res
