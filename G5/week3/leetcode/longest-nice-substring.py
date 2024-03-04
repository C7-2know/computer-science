class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def call(st):
            if len(st)<2:
                return ""
            set_=set(st)
            for i in range(len(st)):
                if st[i].swapcase() not in set_:
                    left= call(st[:i])
                    right= call(st[i+1:])
                    return left if len(left)>=len(right) else right
            else:
                return st
        return call(s)
