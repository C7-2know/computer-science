class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i=1
        st=0
        count=1
        while i<len(points):
            if points[i][0]>points[st][1]:
                st=i
                count+=1
            if points[st][0]>points[i][0]:
                st=i
            if points[st][1]>points[i][1]:
                st=i
            i+=1
        return count
        # points=sorted(points, key=lambda x: x[1])
        # end=points[-1][1]
        # st=points[-1][0]
        # count=1
        # for i in range(len(points)-2,-1,-1):
        #     if points[i][1]>=st and points[i][1]<=end:
        #         st=max(st,points[i][0])
        #         end=min(end,points[i][1])
        #         continue
        #     else:
        #         count+=1
        #         st=points[i][0]
        #         end=points[i][1] 
        # return count
        