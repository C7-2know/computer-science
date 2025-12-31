class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(st, loop):
            if loop== n:
                return st
            j=0
            result =""
            while j<len(st):
                count=0
                l= st[j]
                while j<len(st) and st[j]==l:
                    count+=1
                    j+=1
                if count==0:
                    count+=1
                    j+=1
                result+=f"{count}{l}"
            return rle(result, loop+1)
        return rle("1",1)