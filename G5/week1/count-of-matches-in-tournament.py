import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches=0
        while n>1:
            total_matches+=math.floor(n/2)
            n=math.ceil(n/2)
        return int(total_matches)
        
        
        # while n>1:
        #     match=0
        #     if n%2==0:
        #         match=n/2
        #         n=n/2
        #     else:
        #         match=(n-1)/2
        #         n=(n+1)/2
        #     total_matches+=match
        # return int(total_matches)