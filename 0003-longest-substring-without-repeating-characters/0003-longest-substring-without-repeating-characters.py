class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_=0
        lts=set()
        while r<len(s):
            while s[r] in lts:
                lts.remove(s[l])
                l+=1
            lts.add(s[r])
            max_=max(max_,r-l+1)
            r+=1
        return max_
            
