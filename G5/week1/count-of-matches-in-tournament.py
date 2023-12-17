class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches=0
        while n>1:
            match=0
            if n%2==0:
                match=n/2
                n=n/2
            else:
                match=(n-1)/2
                n=(n+1)/2
            total_matches+=match
        return int(total_matches)