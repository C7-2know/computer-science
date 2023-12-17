class FrequencyTracker:
    def __init__(self):
        # self.List=[]
        self.dict_={}
        self.freq={0:0}
    def add(self, number: int) -> None:
        # self.List.append(number)
        if number not in self.dict_:
            self.dict_[number]=1
            self.freq[1] = self.freq.get(1,0) + 1
        else:
            frq=self.dict_[number]
            self.freq[frq]-=1
            self.dict_[number]+=1
            if frq+1 not in self.freq:
                self.freq[frq+1]=1
            else:
                self.freq[frq+1]+=1
    def deleteOne(self, number: int) -> None:
        occur=False
        if number in self.dict_ and self.dict_[number]>0:
            occur=True
        if occur:
            frq=self.dict_[number]
            print(frq)
            self.freq[frq]-=1
            if frq-1 in self.freq:
                self.freq[frq-1]+=1
            self.dict_[number]-=1

    def hasFrequency(self, frequency: int) -> bool:
    
        if frequency in self.freq and self.freq[frequency]>=1:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)