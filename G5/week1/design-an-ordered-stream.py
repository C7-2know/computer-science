class OrderedStream:

    def __init__(self, n: int):
       self.dict_={} 
       self.ptr=1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.dict_[idKey]=value
        out_pt=[]
        while self.ptr in self.dict_:
            out_pt.append(self.dict_[self.ptr])
            self.ptr+=1
        return out_pt
        
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)