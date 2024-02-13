class Node:
    def __init__(self,val,nxt=None):
        self.val=val
        self.next=nxt
class MyLinkedList:

    def __init__(self):
       self.dummy=Node(0)
       self.size=0 

    def get(self, index: int) -> int:
        curr=self.dummy.next
        if index>=self.size:
            return -1
        else:
            for _ in range(index):
                curr=curr.next
            return curr.val

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.dummy.next
        self.dummy.next=new_node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return -1
        elif index==0:
            self.addAtHead(val)
        else:
            new_node=Node(val)
            curr=self.dummy.next
            for _ in range(index-1):
                curr=curr.next
            new_node.next=curr.next
            curr.next=new_node
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        curr=self.dummy
        if index<self.size:
            for _ in range(index):
                if curr==self.dummy:
                    curr=self.dummy.next
                else:
                    curr=curr.next
            curr.next=curr.next.next
            self.size-=1

            



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)