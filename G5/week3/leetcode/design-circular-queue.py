class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.head=None
        self.tail=None

    def enQueue(self, value: int) -> bool:
        new=Node(value)
        if self.head==None:
            self.head=new
            self.tail=new
            self.size-=1
            return True
        else:
            if self.size!=0:
                new.prev=self.tail
                self.tail.next=new
                self.tail=new
                print(self.head.val,self.head.next.val)
                self.size-=1
                return True
            else:
                return False
    def deQueue(self) -> bool:
        if self.head==None:
            return False
        else:
            if self.head.next!=None:
                # temp=self.head
                self.head=self.head.next
                self.head.prev=None
                # temp.next=None
            else:
                self.head=None
                self.tail=None
            self.size+=1
            return True

    def Front(self) -> int:
        if self.head:
            return self.head.val
        else:
            return -1

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.head==None

    def isFull(self) -> bool:
        return self.size==0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()