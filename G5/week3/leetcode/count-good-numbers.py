
class Solution:

    def countGoodNumbers(self, n: int) -> int:
        # if n%2==0:
        #     return (pow(5,(n//2),(10**9 + 7))*pow(4,(n//2),(10**9 + 7)))%(10**9 + 7)
        # return pow(5,(n//2+1),(10**9 + 7))*pow(4,(n//2),(10**9 + 7))%(10**9 + 7)
        

        even=(n+1)//2
        prime=n//2
        m=10**9+7

        def pow_(x,n):
            if n==0:
                return 1
            if n%2==0:
                return ((pow_(x,n//2)%m)**2 %m)%m
            else:
                return (x*(pow_(x,n//2)%m)**2 %m)%m
        return (pow_(5,even)%m*pow_(4,prime)%m)%m

