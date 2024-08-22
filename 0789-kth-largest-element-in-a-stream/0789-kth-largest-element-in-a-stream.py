class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.lists=[]
        
        for i in range(k):
            if len(nums)>i:
                self.lists.append(nums[i])
        heapify(self.lists)
        self.k=k
        print(nums)

    def add(self, val: int) -> int:
        heappush(self.lists,val)
        min_=heappop(self.lists)
        if len(self.lists)>=self.k:
            min_=heappop(self.lists)
        heappush(self.lists,min_)
        return min_
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)