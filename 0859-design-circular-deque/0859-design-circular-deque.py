class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size=k
        self.start=None
        self.end=None
        self.size=0

    def insertFront(self, value: int) -> bool:
        if self.size==self.max_size:
            return False
        new=Node(value)
        self.size+=1
        if self.end==None:
            self.end=new
            self.start=new
            return True
        new.next=self.start
        self.start.prev=new
        self.start=new
        return True
    def insertLast(self, value: int) -> bool:
        if self.size==self.max_size:
            return False
        new=Node(value)
        self.size+=1
        if not self.end:
            self.end=new
            self.start=new
            return True
        new.prev=self.end
        self.end.next=new
        self.end=new
        return True

    def deleteFront(self) -> bool:
        if self.start==None:
            return False
        self.start=self.start.next
        if self.start:
            self.start.prev=None
        else:
            self.end=None
        self.size-=1
        return True

    def deleteLast(self) -> bool:
        if not self.end:
            return False
        self.end=self.end.prev
        if self.end:
            self.end.next=None
        else:
            self.start=None
        self.size-=1
        return True

    def getFront(self) -> int:
        if not self.start:
            return -1
        return self.start.val

    def getRear(self) -> int:
        if not self.end:
            return -1
        return self.end.val

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()