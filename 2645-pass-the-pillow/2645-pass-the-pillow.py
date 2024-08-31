class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # time+=1
        turn=time//(n-1)
        r=time-(n-1)*turn
        if turn%2==0:
            return 1+r
        else:
            return n-r