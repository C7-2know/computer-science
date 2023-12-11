class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps=0
        for i in range(len(points)-1):
            y_dis=abs(points[i][0]-points[i+1][0])
            x_dis=abs(points[i][1]-points[i+1][1])
            steps+=max(y_dis,x_dis)
        return steps