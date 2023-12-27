class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        colm=[]
        for i in range(len(points)):
            colm.append(points[i][0])
        colm.sort()
        di=0
        for i in range(len(colm)-1):
            di=max(di,colm[i]-colm[i-1])
        return di