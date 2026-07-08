class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dc1={}
        for c in licensePlate:
            c=c.upper()
            if ord(c)<65 or ord(c)>90:
                continue
            if c not in dc1:
                dc1[c]=0
            dc1[c]+=1
        dc2=dc1
        ans=[]
        words.sort(key=lambda x:len(x))
        for word in words:
            dc2=dc1.copy()
            for c in word:
                if c.upper() in dc2:
                    dc2[c.upper()]-=1
            if max(dc2.values())<=0:
                return word
        