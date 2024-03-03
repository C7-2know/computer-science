class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dc={}
        for i in t:
            t_dc[i]=t_dc.get(i,0)+1
        s_dc=t_dc
        # s+='0'
        min_=float('inf')
        min_s=''
        left=0
        needed=len(t)
        for j in range(len(s)):
            if s[j] in t_dc:
                s_dc[s[j]]-=1
            while max(s_dc.values())<=0:
                if j-left<min_:
                    min_s=s[left:j+1]
                    min_=j-left
                if s[left] in s_dc:
                    s_dc[s[left]]+=1
                left+=1
        return min_s