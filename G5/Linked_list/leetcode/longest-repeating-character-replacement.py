class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dc={}
        left=0
        long=0
        for i in range(len(s)):
            dc[s[i]]=dc.get(s[i],0)+1
            while sum(dc.values())-max(dc.values())>k and len(dc)>1:
                dc[s[left]]-=1
                if dc[s[left]]==0:
                    dc.pop(s[left])
                # if dc[s[left]]==min(dc.values()):
                #     k+=1
                left+=1
            long=max(long,sum(dc.values()))
        return long