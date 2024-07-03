class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        parent=[i for i in range(n)]
        parent[firstPerson]=0
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        
        def union(x,y):
            px=find(x)
            py=find(y)
            parent[px]=0
            parent[py]=0
        
        i=0
        persons=set([firstPerson,0])
        while i<len(meetings):
            t=meetings[i][2]
            ch={}
            while i<len(meetings) and meetings[i][2]==t:
                p1,p2=find(meetings[i][0]),find(meetings[i][1])
                # print('here',p1,p2,parent)
                visited=set()
                if p1==0 or p2==0:
                    union(p1,p2)
                    persons.add(p1)
                    persons.add(p2)
                    if p1 in ch:
                        queue=ch[p1]
                        visited.add(p1)
                        while queue:
                            c=queue.pop()
                            union(p1,c)
                            persons.add(c)
                            if c in ch and c not in visited:
                                queue.extend(ch[c])
                            visited.add(c)
                    if p2 in ch:
                        queue=ch[p2]
                        visited.add(p2)
                        while queue:
                            c=queue.pop()
                            union(p2,c)
                            persons.add(c)
                            if c in ch and c not in visited:
                                queue.extend(ch[c])
                            visited.add(c)

                else:
                    if p1 not in ch:
                        ch[p1]=[]
                    ch[p1].append(p2)
                    if p2 not in ch:
                        ch[p2]=[]
                    ch[p2].append(p1)

                i+=1
            # print(ch)
        return list(persons)
        

        
        