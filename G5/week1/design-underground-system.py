class UndergroundSystem:

    def __init__(self):
        self.checkIn_={}
        self.checkOuts={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIn_[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation=self.checkIn_[id][0]
        time=self.checkIn_[id][1]
        if f'{startStation},{stationName}' not in self.checkOuts:
            self.checkOuts[f'{startStation},{stationName}']=[0,0]
        self.checkOuts[f'{startStation},{stationName}'][0]+=(t-time)
        self.checkOuts[f'{startStation},{stationName}'][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time=self.checkOuts[f'{startStation},{endStation}'][0]
        freq=self.checkOuts[f'{startStation},{endStation}'][1]
        return time/freq
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)