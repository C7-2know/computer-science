class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ch=0
        coki=0
        while ch<len(g) and coki<len(s):
            if g[ch]<=s[coki]:
                ch+=1
                coki+=1
            else:
                coki+=1
        return ch