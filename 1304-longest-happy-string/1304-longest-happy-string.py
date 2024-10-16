class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        if a>0:
            heap.append((-a,"a"))
        if b>0:
            heap.append((-b,"b"))
        if c>0:
            heap.append((-c,"c"))
        heapify(heap)
        ans=""
        print("st",heap)
        while heap:
            n,c= heappop(heap)
            n*=-1
            if ans and ans[-1]==c:
                if not  heap:
                    return ans
                nn,cc=heappop(heap)
                nn*=-1
                ans+=cc
                nn-=1
                if nn>0 and n/nn<=2:
                    ans+=cc
                    nn-=1
                if nn>0:
                    heappush(heap,(-nn,cc))
            else:
                ans+=c
                n-=1
                if heap and n>0:
                    ans+=c
                    n-=1
                elif n>0:
                    ans+=c
                    n-=1
            if n>0:
                heappush(heap,(-n,c))
            print(heap,ans)
        return ans
                