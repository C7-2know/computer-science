class Solution:
    def __init__(self):
        self.dc={}
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        if n in self.dc:
            return self.dc[n]
        num=self.fib(n-1)+self.fib(n-2)
        self.dc[n]=num
        return num

        # a,b=0,1
        # s=0
        # if n<2:
        #     return n
        # for i in range(2,n):
        #     s=a+b
        #     a=b
        #     b=s
        # return b