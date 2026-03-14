class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dc = {}
        seen = set()
        s=s.split(' ')
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dc and s[i] not in seen:
                dc[pattern[i]]= s[i]
                seen.add(s[i])
            if pattern[i] not in dc or dc[pattern[i]] != s[i]:
                return False
        return True
