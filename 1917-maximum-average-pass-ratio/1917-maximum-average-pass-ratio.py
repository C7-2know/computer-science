class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        temp=[]
        for a,b in classes:
            ratio=(a-b)/((b)*(b+1))
            heapq.heappush(temp,[ratio,a,b])
        while extraStudents>0:
            ratio,a,b=heapq.heappop(temp)
            a=a+1
            b=b+1
            extraStudents-=1
            ratio=(a-b)/((b)*(b+1))
            heapq.heappush(temp,[ratio,a,b])
        ans=0.00000
        #print(temp)
        while temp:
            _,a,b=heapq.heappop(temp)
            ans+=a/b
        return ans/len(classes)