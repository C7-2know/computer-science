class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        size=[1 for i in range(n)]

        def find(a):
            while parent[a]!=a:
                a=parent[a]
            return a

        def union(a,b):
            p_a=find(a)
            p_b=find(b)
            if p_a==p_b:
                return
            if size[p_a]>size[p_b]:
                parent[p_b]=p_a
                size[p_a]+=size[p_b]
            else:
                parent[p_a]=p_b
                size[p_b]+=size[p_a]
        
        for i in edges:
            union(i[0],i[1])
        conn=set()
        for i in parent:
            conn.add(find(i))
        conn=list(conn)
        pre=[size[conn[i]] for  i in range(len(conn))]
        for i in range(len(pre)-2,-1,-1):
            pre[i]+=pre[i+1]
        pair=0

        print(conn)
        print(size)
        for i in range(len(conn)-2,-1,-1):
            pair+=(pre[i+1]*size[conn[i]])
            # pre=pre*size[conn[i]]
        return pair