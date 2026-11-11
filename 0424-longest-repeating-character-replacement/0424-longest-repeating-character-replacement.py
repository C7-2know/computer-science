class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_=0
        l,r=0,0
        count={}
        while r<len(s):
            if s[r] not in count:
                count[s[r]]=0
            count[s[r]]+=1
            while max(count.values())+k<(r-l+1):
                count[s[l]]-=1
                l+=1
            max_=max(max_, r-l+1)
            r+=1
        return max_