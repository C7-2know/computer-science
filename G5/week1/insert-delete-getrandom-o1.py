class RandomizedSet:

    def __init__(self):
        self.set={}

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set[val]=1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        rand=randint(0,len(self.set.keys())-1)
        sett=list(self.set.keys())
        return sett[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()