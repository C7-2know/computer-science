class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        pre=[[] for _ in range(n+1)]
        pre_num=[0]*(n+1)
        for i in relations:
            pre[i[0]].append(i[1])
            pre_num[i[1]]+=1
        queue=[]
        for j in range(1,n+1):
            if pre_num[j]==0:
                queue.append(j)
        
        ans=0
        pre_max=0
        before=[0]+time.copy()
        while queue:
            next_=[]
            for i in range(len(queue)):
                node=queue[i]
                for nei in pre[node]:
                    pre_num[nei]-=1
                    before[nei]=max(before[nei],time[nei-1]+before[node])

                    if pre_num[nei]==0:
                        next_.append(nei)
            queue=next_

        return max(before)
