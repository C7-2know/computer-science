class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x=n
        print(x%(n*2)==0)
        if x%2==0:
            return x
        else:
            mult=0
            while x%(n*2)!=0:
                x+=1
            return x