class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq=int(sqrt(c))
        st,end=0,sq
        while st<=end:
            if st**2+end**2==c:
                return True
            elif st**2+end**2>c:
                end-=1
            else:
                st+=1
        return False