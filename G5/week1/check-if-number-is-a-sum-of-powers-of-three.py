class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n%3>1:
            return False
        num=0
        max_power=20
        for i in range(max_power,-1,-1):
            if n-3**i>=0:
                n=n-3**i
            else:
                continue
        return n==0

        
        # for i in range(n//3):
        #     num+=3
        #     print(num)
        #     if num==n:
        #         return True
        #     elif num+1==n:
        #         return True
        # else:
        #     return False

        #     substract