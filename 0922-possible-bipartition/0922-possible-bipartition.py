class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dc={}
        for pair in dislikes:
            if pair[0] not in dc:
                dc[pair[0]]=[]
            if pair[1] not in dc:
                dc[pair[1]]=[]
            dc[pair[0]].append(pair[1])
            dc[pair[1]].append(pair[0])
        # print(dc)

        color=[0 for _ in range(n+1)]
        for k in dc:
            if color[k]!=0:
                continue
            queue=deque([k])
            color[k]=1
            while queue:
                num=queue.pop()
                c=2
                if color[num]==2:
                    c=1                    
                if num not in dc:
                    continue
                for nbr in dc[num]:
                    if color[nbr]!=0 and color[nbr]!=c:
                        print(color)
                        return False
                    if color[nbr]==0:
                        color[nbr]=c
                        queue.append(nbr)
        return True

