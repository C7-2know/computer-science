class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.stack=[]

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)<1:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        k=min(k,len(self.stack))
        for i in range(k):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)