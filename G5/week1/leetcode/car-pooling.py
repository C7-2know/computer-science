class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_=float('-inf')
        min_=float('inf')
        for i in range(len(trips)):
            max_=max(trips[i][2],max_)
            min_=min(trips[i][1],min_)
        trip=[0 for i in range(min_,max_+1)]
        for j in range(len(trips)):
            st=trips[j][1]-min_
            end=trips[j][2]-min_
            trip[st]+=trips[j][0]
            if end+1<len(trip):
                trip[end]-=trips[j][0]
        total=0
        # print('trip',trip)
        for k in range(len(trip)):
            total+=trip[k]
            trip[k]=total
            if trip[k]>capacity:
                # print(trip)
                return False
        else:
            # print(trip)
            return True
