class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for i in s:
            num+=str(ord(i)-96)
        def add(st):
            res=0
            for i in st:
                res+=int(i)
            return res
        for i in range(k):
            num=str(add(num))
        return int(num)
