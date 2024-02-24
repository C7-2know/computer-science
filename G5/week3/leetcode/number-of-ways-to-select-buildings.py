class Solution:
    def numberOfWays(self, s: str) -> int:
        pref=[0 for i in range(len(s))]
        c0=0
        c1=0
        for k in range(len(s)):
            if s[k]=='1':
                pref[k]=c0
                c1+=1
            else:
                pref[k]=c1
                c0+=1
        count=0
        # print(pref)
        for i in range(len(pref)):
            if s[i]=='1':
                count+=(pref[i]*(c0-pref[i]))
            else:
                count+=(pref[i]*(c1-pref[i]))
        return count
            