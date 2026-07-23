class Solution:
    def frequencySort(self, s: str) -> str:
        dc={}
        for c in s:
            if c not in dc:
                dc[c]=0
            dc[c]+=1
        arr=[]
        heapq.heapify(arr)
        for k,v in dc.items():
            heapq.heappush(arr, (-1*v,k))

        ans=''
        while arr:
            v,c=heapq.heappop(arr)
            ans+=(c*(-1*v))
        return ans