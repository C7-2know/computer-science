class Solution:
    def isHappy(self, n: int) -> bool:
        i=0
        n=str(n)
        loop=0
        while i!=1:
            i=0
            for j in range(len(n)):
                i+=int(n[j])**2
            n=str(i)
            print(n)
            loop+=1
            if loop==100:
                return False
        return True
        
