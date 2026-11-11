class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_=0
        l,r=0,0
        count={}
        max_f=0
        while r<len(s):
            if s[r] not in count:
                count[s[r]]=0
            count[s[r]]+=1
            max_f=max(max_f, count[s[r]])
            while max_f+k<(r-l+1):
                count[s[l]]-=1
                l+=1
            max_=max(max_, r-l+1)
            r+=1
        return max_