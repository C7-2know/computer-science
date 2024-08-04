class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent=[i for i in range(len(s))]
        size=[1 for _ in range(len(s))]
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[parent[x]]
            return x
        def union(x,y):
            px,py=find(x),find(y)
            if size[px]>size[py]:
                parent[py]=px
                size[px]+=size[py]
            else:
                parent[px]=py
                size[py]+=size[px]

        for p in pairs:
            union(p[1],p[0])

        group={}

        for elm in range(len(parent)):
            p=find(elm)
            if p not in group:
                group[p]=[]
            group[p].append(elm)
        res="*"*len(s)
        print(group)
        for p in group:
            group[p].sort()
            word=[s[i] for i in group[p]]
            word.sort()
            for i in range(len(group[p])):
                ind=group[p][i]
                res=res[:ind]+word[i]+res[ind+1:]
        return res