class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[-1*i for i in gifts]
        heapify(heap)
        while k>0:
            cur=sqrt(-1*heappop(heap))
            heappush(heap,-1*math.floor(cur))
            k-=1
        return -1*sum(heap)