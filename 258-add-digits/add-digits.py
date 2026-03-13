class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        res=int(num)
        while len(num)>1:
            res=0
            for i in num:
                res+=int(i)
            num=str(res)
        return res