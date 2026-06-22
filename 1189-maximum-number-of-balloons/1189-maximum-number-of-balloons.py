class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dc={}
        word=set(['b', 'a', 'l','o','n'])
        for c in text:
            if c in word:
                if c not in dc:
                    dc[c]=0
                dc[c]+=1
        if len(dc.keys())!=len(word):
            return 0
        res=float('inf')
        for key, val in dc.items():
            if key=='o' or key=='l':
                res=min(res,val//2)
            else:
                res=min(res,val)
        return res
