class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        dc={s[0]:1}
        i,j=0,1
        max_=1
        while j<len(s):
            if s[j] not in dc:
                dc[s[j]]=0
            dc[s[j]]+=1
            while dc[s[j]]>2:
                dc[s[i]]-=1
                i+=1
            max_=max(max_,j-i+1)
            j+=1
        return max_