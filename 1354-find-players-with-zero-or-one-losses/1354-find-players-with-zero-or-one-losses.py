class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        point={}
        lose={}
        for i in range(len(matches)):
            win=matches[i][0]
            los=matches[i][1]
            if win not in point:
                point[win]=[0,0]
            point[win][0]+=1
            if los not in point:
                point[los]=[0,0]
            point[los][1]+=1
        ans=[[],[]]
        for i in point:
            if point[i][1]==0:
                ans[0].append(i)
            if point[i][1]==1:
                ans[1].append(i)  
        ans[0].sort()
        ans[1].sort()          
        return ans