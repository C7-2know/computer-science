class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {a:a for a in string.ascii_lowercase}

        def find(x):
            while x!= root[x]:
                x = root[root[x]]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)
            root[px]= py
        
        for eq in equations:
            eq.lower()
            if eq[1]== "=":
                union(eq[0], eq[3])
            elif find(eq[0])== find(eq[3]):
                return False
        for eq in equations:
            eq.lower()
            if eq[1]== "=":
                pass 
            elif find(eq[0])== find(eq[3]):
                return False
        return True
            