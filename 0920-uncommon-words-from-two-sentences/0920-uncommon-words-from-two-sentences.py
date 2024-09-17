class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        tot=list(s1.split(" "))+list(s2.split(" "))
        tot.sort()
        visited=set()
        res=[]
        for w in tot:
            if w in visited and res and res[-1]==w:
                res.pop()
            elif w not in visited:
                res.append(w)
            visited.add(w)
        return res