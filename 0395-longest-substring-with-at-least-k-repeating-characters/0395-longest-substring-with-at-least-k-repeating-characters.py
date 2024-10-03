class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dc={}
        def is_sub(s,k):
            for i in dc:
                if dc[i]<k:
                    return False
            return True
        max_=0
        for i in range(len(s)):
            dc={}
            for j in range(i,len(s)):
                if s[j] not in dc:
                    dc[s[j]]=0
                dc[s[j]]+=1
                if is_sub(s[i:j+1],k):
                    max_=max(max_,j-i+1)
        return max_

            