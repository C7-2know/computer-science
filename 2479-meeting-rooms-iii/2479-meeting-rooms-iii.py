class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms=[]
        count=[0]*n
        meetings.sort()
        print(meetings)
        for i in range(n):
            rooms.append((0,i))
        print('start',rooms)
        heapify(rooms)
        for meet in meetings:
            t,i=heappop(rooms)
            loop=True
            temp=[]
            while loop and rooms:
                nt,ni=heappop(rooms)
                if nt>meet[0]:
                    heappush(rooms,(nt,ni))
                    loop=False
                elif ni<i:
                    temp.append((t,i))
                    t,i=nt,ni
                else:
                    temp.append((nt,ni))
            
            rooms.extend(temp)
            heapify(rooms)
            if meet[0]<t:
                t+=(meet[1]-meet[0])
            else:
                t=meet[1]
            heappush(rooms,(t,i))
            # print('rooms',rooms)
            count[i]+=1
        
        max_=max(count)
        print(count)
        for i in range(n):
            if count[i]==max_:
                return i
        