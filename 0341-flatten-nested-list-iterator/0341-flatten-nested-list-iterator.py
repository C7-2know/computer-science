# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.pointer = 0
        def flat(lst):
            for i in lst:
                if i.isInteger():
                    self.list.append(i)
                else:
                    list_= i.getList()
                    flat(list_)
                    
        flat(nestedList)

    def next(self) -> int:
        val = self.list[self.pointer]
        self.pointer+=1
        return val

    
    def hasNext(self) -> bool:
        return True if self.pointer < len(self.list) else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())