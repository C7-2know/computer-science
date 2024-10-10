class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inwards={}
        for fly in flights:
            if fly[1] not in inwards:
                inwards[fly[1]]=[]
            inwards[fly[1]].append((fly[2],fly[0]))
        print(inwards)
        prev=[float('inf') for _ in range(n)]
        curr=[float('inf') for _ in range(n)]
        prev[src]=0
        for i in range(k+1):
            for j in range(n):
                if j not in inwards:
                    continue
                for w,u in inwards[j]:
                    curr[j]=min(curr[j],w+prev[u])
            prev=curr.copy()
        
        return curr[dst] if curr[dst]!=float('inf') else -1

        

