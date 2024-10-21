class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverse(x):
            return x[::-1]
        def invert(x):
            new='1'*len(x)
            new=int("0b"+new,2)
            x=int("0b"+x,2)
            return bin(new^x)[2:]
        def rec(x):
            if x==1:
                return "0"
            res=rec(x-1)
            return res+"1"+inverse(invert(res))
        sn=rec(n)
        return sn[k-1]
