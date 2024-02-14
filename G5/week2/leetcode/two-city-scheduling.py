class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        profit=[costs[i][0]-costs[i][1] for i in range(len(costs))]
        dc={}
        for a,b in (enumerate(profit)):
            if b not in dc:
                dc[b]=[]
            dc[b].append(a)
        profit.sort()
        # print(dc)
        cost=0
        # print(dc)
        for i in range(len(costs)):
            ind=dc[profit[i]].pop()
            cos=costs[ind][0]
            if i>=len(costs)/2:
                cos=costs[ind][1]
            cost+=cos
        return cost