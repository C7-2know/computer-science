class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost=0
        l,r=0,0
        max_=0
        while r<len(s):
            while cost+abs(ord(s[r])-ord(t[r]))>maxCost:
                cost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            cost+=abs(ord(s[r])-ord(t[r]))
            r+=1
            max_=max(max_,r-l)
        return max_
            