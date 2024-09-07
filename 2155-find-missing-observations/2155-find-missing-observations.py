class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        x=mean*(len(rolls)+n)-sum(rolls)
        if x<=0 or x//n>6 or (x//n==6 and x%n!=0) or x//n==0:
            return []
        if x%n==0:
            return [x//n]*n
        res=[x//n]*(n-1)
        last=x//n+x%n
        i=0
        while last>6 and i<len(res):
            last-=(6-res[i])
            res[i]=6
            i+=1
        res.append(last)
        return res