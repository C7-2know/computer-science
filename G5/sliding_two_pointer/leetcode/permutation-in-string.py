class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1={}
        n=len(s1)
        ds2={}
        for i in range(n):
            if i>=len(s2):
                return False
            ds1[s1[i]]=ds1.get(s1[i],0)+1
            ds2[s2[i]]=ds2.get(s2[i],0)+1
        if ds1==ds2:
            return True
        for k in range(n,len(s2)):
            ds2[s2[k-n]]-=1
            if ds2[s2[k-n]]==0:
                ds2.pop(s2[k-n])
            ds2[s2[k]]=ds2.get(s2[k],0)+1
            if ds2==ds1:
                return True
        else:
            return False