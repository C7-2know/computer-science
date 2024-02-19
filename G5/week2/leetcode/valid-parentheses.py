class Solution:
    def isValid(self, s: str) -> bool:
        dc={'(':')','[':']','{':'}'}
        store=[]
        for i in range(len(s)):
            if s[i] in dc:
                store.append(s[i])
            else:
                if len(store)==0:
                    return False
                if dc[store[-1]]!=s[i]:
                    return False
                store.pop()
        if len(store)!=0:
            return False
        return True