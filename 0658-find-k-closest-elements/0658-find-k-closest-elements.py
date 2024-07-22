class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        heapify(heap)
        for i in range(len(arr)):
            heappush(heap,(abs(arr[i]-x),arr[i]))
        res=[]
        heapify(res)
        while len(res)<k:
            heappush(res,heappop(heap)[1])
       
        res.sort()
        return res