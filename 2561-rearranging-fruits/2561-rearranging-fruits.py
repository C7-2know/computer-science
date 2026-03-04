class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        frq={}
        for i in basket1:
            if i not in frq:
                frq[i]=[0,0]
            frq[i][0]+=1
        for i in basket2:
            if i not in frq:
                frq[i]=[0,0]
            frq[i][1]+=1
        b2=[]
        b1=[]
        min_=float('inf')
        for k,val in frq.items():
            df=val[0]-val[1]
            if df!=0:
                if df%2!=0:
                    return -1
                if df>0:
                    b1.append((k,df//2))
                else:
                    b2.append((k,-1*df//2))
            min_=min(min_,k)
        b1.sort()
        b2.sort()
        i=0
        tot=0
        while b1:
            cost,f=b1.pop()
            while f>0:
                c2,f2=b2[i]
                min_c=min(cost,c2)
                if min_c>2*min_:
                    tot+=min_*f
                    f=0
                    continue
                if f2>f:
                    tot+=min_c*f
                    f2-=f
                    b2[i]=(c2,f2)
                    f=0
                else:
                    tot+=min_c*f2
                    f-=f2
                    f2=0
                    b2[i]=(c2,0)
                    i+=1
        while i<len(b2):
            cost,f2=b2[i]
            tot+=min_*f2
            i+=1

        return tot
            


        
                