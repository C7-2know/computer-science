class Solution:
    def splitString(self, s: str) -> bool:
        def bt(st,l,ls):
            if l>=len(st):
                return True
            for i in range(l,len(st)):
                if int(st[l:i+1])==ls-1:
                    if bt(st,i+1,int(st[l:i+1])):
                        return True
                if int(st[l:i+1])>ls:
                    return False
            return False
                
        for i in range(len(s)-1):
            res=bt(s,i+1,int(s[:i+1]))
            if res:
                return True
        else:
            return False
