class Solution:
    def processStr(self, s: str) -> str:
        res=''
        for i in s:
            if i=='*':
                if not res:
                    continue
                res=res[:-1]
            elif i=='#':
                res+=res
            elif i=='%':
                res=res[::-1]
            else:
                res+=i
        return res