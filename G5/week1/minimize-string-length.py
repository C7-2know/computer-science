class Solution:
    def minimizedStringLength(self, s: str) -> int:
        j=1
        while j<len(s):
            if s[j] in s[:j]:
                prev=s[:j].index(s[j])
                s=s[:prev]+s[prev+1:]
            else:
                j+=1
        return len(s)