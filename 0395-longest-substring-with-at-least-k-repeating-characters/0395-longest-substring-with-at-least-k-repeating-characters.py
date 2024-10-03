class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for char in set(s):
            if s.count(char)<k:
                max_=0
                for sub in s.split(char):
                    max_=max(max_,self.longestSubstring(sub,k))
                return max_
        return len(s)
            