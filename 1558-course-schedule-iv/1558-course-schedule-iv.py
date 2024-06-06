class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pres=[0 for i in range(numCourses)]
        graph={}
        for i in prerequisites:
            pres[i[1]]+=1
            if i[0] not in graph:
                graph[i[0]]=[]
            graph[i[0]].append(i[1])
        queue=[]

        for i in range(len(pres)):
            if pres[i]==0:
                queue.append(i)
        count=0
        order=[set() for _ in range(numCourses)]

        ind=0
        while queue:
            size=len(queue)
            node=queue.pop()
            if node not in graph:
                continue
            for nbr in graph[node]:
                pres[nbr]-=1
                if pres[nbr]==0:
                    queue.append(nbr)
                order[nbr].add(node)
                order[nbr]=order[nbr].union((order[node]))
        out=[]
        for i in queries:
            if i[0] in order[i[1]]:
                out.append(True)
            else:
                out.append(False)

        return out
            