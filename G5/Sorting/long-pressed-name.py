class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        dc={}
        # for i in name:
        #     dc[i]=dc.get(i,0)+1
        # for j in typed:
        #     if dc.get(j,0)<1:
        #         return False
        #     elif dc.get(j,0)>1:
        #         dc[j]-=1
        #     else:
        #         dc.pop(j)
        # print('dcc')
        # return len(dc)==0
        first=0
        sec=0
        while first<len(name):
            if name[first]!=typed[sec]:
                if first==0 or name[first-1]!=typed[sec]:
                    return False
                sec+=1
            else:
                first+=1
                sec+=1
            if sec>=len(typed) and first<len(name):
                return False
        # print(typed[sec:],name[first-1],typed[sec:].count(name[first-1]))
        if sec<len(typed):
            return len(typed[sec:])==typed[sec:].count(name[first-1])
        return True
