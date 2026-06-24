class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        p1,p2=0,len(s)-1
        while p1<=p2:
            if s[p1]==s[p2]:
                return p1
            p1+=1
            p2-=1
        return -1