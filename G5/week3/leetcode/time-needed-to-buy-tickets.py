class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque()
        time=0
        for i in range(len(tickets)):
            if tickets[i]!=0:
                queue.append(i)
        while queue:
            front=queue.popleft()
            tickets[front]-=1
            time+=1
            # print(time,queue,tickets[front])
            if tickets[front]!=0:
                queue.append(front)
            else:
                if front==k:
                    return time
        
                    
        