class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i=0
        tot=0
        while i<len(cost):
            tot+=cost[i]+(cost[i+1] if i+1<len(cost) else 0)
            i+=3
        return tot