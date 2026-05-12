class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans=[]
        for q in queries:
            p2=0
            for c in q:
                if p2<len(pattern) and c==pattern[p2]:
                    p2+=1
                elif ord(c)<91:
                    ans.append(False)
                    break
            else:
                if  p2<len(pattern):
                    ans.append(False)
                else:
                    ans.append(True)
                
        return ans
