class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits=[-1*i for i in profits]
        c_p=list(zip(capital,profits))
        c_p.sort()
        poss=[]
        heapify(poss)
        ind=0
        while k and len(c_p)>0:
            while ind<len(c_p) and w>=c_p[ind][0]:
                heappush(poss,c_p[ind][1])
                ind+=1
            if poss:
                p=heappop(poss)
                w+=(-1*p)
            k-=1
        while k and poss:
            p=heappop(poss)
            w+=(-1*p)
            k-=1
        return w
