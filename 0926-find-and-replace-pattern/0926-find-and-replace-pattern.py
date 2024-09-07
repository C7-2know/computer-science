class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def match(w):
            dc={}
            for i in range(len(w)):
                if w[i] in dc:
                    if dc[w[i]]!=pattern[i]:
                        return False
                else:
                    dc[w[i]]=pattern[i]
            return True
        pat_set=set([l for l in pattern])
        res=[]
        for w in words:
            set_=set([l for l in w])
            if len(set_)==len(pat_set):
                if match(w):
                    res.append(w)
                
        return res
