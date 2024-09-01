class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins=[(arrays[i][0],i) for i in range(len(arrays))]        
        maxs=[(arrays[i][-1],i) for i in range(len(arrays))]
        mins.sort(key=lambda x:x[0])        
        maxs.sort(key=lambda x:x[0]) 
        if maxs[-1][1] ==mins[0][1]:
            d1=abs(maxs[-1][0]-mins[1][0])
            d2=abs(maxs[-2][0]-mins[0][0])
            return max(d1,d2)
        return abs(maxs[-1][0]-mins[0][0])