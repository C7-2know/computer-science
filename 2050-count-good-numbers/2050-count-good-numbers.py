class Solution:
    def countGoodNumbers(self, n: int) -> int:
        pn=ceil(n/2)
        en=n//2
        def bin_exp(base,n):
            result=1
            while n>0:
                if n&1:
                    result=(result*base)%(10**9 + 7)
                base=(base*base)%(10**9+7)
                n=n>>1
            return result
        return (bin_exp(5,ceil(n/2))*bin_exp(4,n//2))%(10**9 + 7)