class Solution:
    def minLength(self, s: str) -> int:
        s.split("AB")
        s.split("CD")
        pre=len(s)
        nw=pre
        while True:
            s="".join(s.split("AB"))
            s="".join(s.split("CD"))
            if len(s)==pre:
                break
            pre=len(s)
        return len(s)