class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key=lambda x: x[1])
        # print(points)
        end=points[-1][1]
        st=points[-1][0]
        count=1
        for i in range(len(points)-2,-1,-1):
            if points[i][1]>=st and points[i][1]<=end:
                st=max(st,points[i][0])
                end=min(end,points[i][1])
                continue
            else:
                count+=1
                st=points[i][0]
                end=points[i][1] 
        return count