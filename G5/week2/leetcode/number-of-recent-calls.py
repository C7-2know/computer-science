class RecentCounter:

    def __init__(self):
        # self.counter=[]
        self.counter=deque()
    def ping(self, t: int) -> int:
        # start=t-3000
        # while self.counter and self.counter[0]<start:
        #     self.counter.pop(0)
        # self.counter.append(t)
        # return len(self.counter)

        start=t-3000
        while self.counter and self.counter[0]<start:
            self.counter.popleft()
        self.counter.append(t)
        return len(self.counter)
            



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)