class MyCalendar:

    def __init__(self):
        self.calander=[]

    def book(self, start: int, end: int) -> bool:
        l,r=0,len(self.calander)-1
        for i in self.calander:
            st,e=i
            if st>end:
                break
            if (start<e and end>st) or start<e and end>=e:
                return False
            
        self.calander.append((start,end))
        self.calander.sort()
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)