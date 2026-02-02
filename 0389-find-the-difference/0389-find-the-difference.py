class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        i = 0
        while i < len(s):
            if s[i]!=t[i]:
                if t[i+1]==s[i]:
                    return t[i]
                return s[i]
            i+=1
        return t[-1]