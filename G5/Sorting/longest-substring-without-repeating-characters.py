class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_st=0
        left=0
        i=0
        dc={}
        while i < len(s):
            if s[i] in dc:
                dc.pop(s[left])
                left+=1
            else:
                dc[s[i]]=1
                max_st=max(i-left+1,max_st)
                i+=1

        return max_st